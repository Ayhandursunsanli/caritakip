from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Fatura
from .forms import FaturaForm
from tedarikciler.models import Tedarikci
from django.http import HttpResponse
import xlsxwriter
from io import BytesIO
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def fatura_listesi(request):
    faturalar = Fatura.objects.all()
    tedarikci_id = request.GET.get('tedarikci')
    fatura_tarihi1 = request.GET.get('fatura_tarihi1')
    fatura_tarihi2 = request.GET.get('fatura_tarihi2')
    odeme_tarihi1 = request.GET.get('odeme_tarihi1')
    odeme_tarihi2 = request.GET.get('odeme_tarihi2')

    if tedarikci_id:
        faturalar = faturalar.filter(tedarikci_id=tedarikci_id)
    if fatura_tarihi1:
        faturalar = faturalar.filter(fatura_tarihi__gte=fatura_tarihi1)
    if fatura_tarihi2:
        faturalar = faturalar.filter(fatura_tarihi__lte=fatura_tarihi2)
    if odeme_tarihi1:
        faturalar = faturalar.filter(odeme_tarihi__gte=odeme_tarihi1)
    if odeme_tarihi2:
        faturalar = faturalar.filter(odeme_tarihi__lte=odeme_tarihi2)

    # Sadece tabloda görünen tedarikçiler
    tedarikciler = Tedarikci.objects.filter(id__in=faturalar.values_list('tedarikci_id', flat=True).distinct())

    context = {
        'faturalar': faturalar,
        'tedarikciler': tedarikciler,
        'filtre': {
            'tedarikci': tedarikci_id,
            'fatura_tarihi1': fatura_tarihi1,
            'fatura_tarihi2': fatura_tarihi2,
            'odeme_tarihi1': odeme_tarihi1,
            'odeme_tarihi2': odeme_tarihi2,
        }
    }
    return render(request, 'faturalar/fatura_listesi.html', context)

@login_required
def fatura_detay(request, pk):
    fatura = get_object_or_404(Fatura, pk=pk)
    return render(request, 'faturalar/fatura_detay.html', {'fatura': fatura})

@login_required
def fatura_ekle(request):
    tedarikci_id = request.GET.get('tedarikci')
    tedarikci = None
    if tedarikci_id:
        tedarikci = get_object_or_404(Tedarikci, pk=tedarikci_id)
    if request.method == "POST":
        form = FaturaForm(request.POST, request.FILES, tedarikci=tedarikci)
        if form.is_valid():
            fatura = form.save(commit=False)
            fatura.tedarikci = tedarikci
            fatura.save()
            form.save_m2m()
            for s in form.cleaned_data['satinalmalar']:
                s.faturaya_baglandi = True
                s.save()
            return redirect('faturalar:fatura_listesi')
    else:
        form = FaturaForm(tedarikci=tedarikci)
        if tedarikci:
            form.fields['tedarikci'].initial = str(tedarikci)
            form.fields['tedarikci'].widget.attrs['value'] = str(tedarikci)
    return render(request, 'faturalar/fatura_form.html', {'form': form})

@login_required
def fatura_duzenle(request, pk):
    fatura = get_object_or_404(Fatura, pk=pk)
    if request.method == "POST":
        form = FaturaForm(request.POST, instance=fatura)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fatura başarıyla güncellendi.')
            return redirect('faturalar:fatura_listesi')
    else:
        form = FaturaForm(instance=fatura)
    return render(request, 'faturalar/fatura_form.html', {'form': form})

@login_required
def fatura_sil(request, pk):
    fatura = get_object_or_404(Fatura, pk=pk)
    if request.method == "POST":
        fatura.delete()
        messages.success(request, 'Fatura başarıyla silindi.')
        return redirect('faturalar:fatura_listesi')
    return render(request, 'faturalar/fatura_sil.html', {'fatura': fatura})

def fatura_listesi_excel(request):
    faturalar = Fatura.objects.all()
    tedarikci_id = request.GET.get('tedarikci')
    fatura_tarihi1 = request.GET.get('fatura_tarihi1')
    fatura_tarihi2 = request.GET.get('fatura_tarihi2')
    odeme_tarihi1 = request.GET.get('odeme_tarihi1')
    odeme_tarihi2 = request.GET.get('odeme_tarihi2')

    if tedarikci_id:
        faturalar = faturalar.filter(tedarikci_id=tedarikci_id)
    if fatura_tarihi1:
        faturalar = faturalar.filter(fatura_tarihi__gte=fatura_tarihi1)
    if fatura_tarihi2:
        faturalar = faturalar.filter(fatura_tarihi__lte=fatura_tarihi2)
    if odeme_tarihi1:
        faturalar = faturalar.filter(odeme_tarihi__gte=odeme_tarihi1)
    if odeme_tarihi2:
        faturalar = faturalar.filter(odeme_tarihi__lte=odeme_tarihi2)

    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    headers = ['Fatura No', 'Tedarikçi', 'Fatura Tarihi', 'Ödeme Tarihi', 'Tutar']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)
    for row, f in enumerate(faturalar, start=1):
        worksheet.write(row, 0, f.fatura_no)
        worksheet.write(row, 1, f.tedarikci.ad)
        worksheet.write(row, 2, f.fatura_tarihi.strftime('%d.%m.%Y'))
        worksheet.write(row, 3, f.odeme_tarihi.strftime('%d.%m.%Y'))
        worksheet.write(row, 4, float(f.tutar))
    workbook.close()
    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=fatura_listesi.xlsx'
    return response 