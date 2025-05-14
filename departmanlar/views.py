# departmanlar/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Departman
from .forms import DepartmanForm
from satin_alma.models import SatinAlma
from urunler.models import Urun
from tedarikciler.models import Tedarikci
from django.db.models import Sum
from django.http import HttpResponse
import xlsxwriter
from io import BytesIO

def departman_listesi(request):
    departmanlar = Departman.objects.all()
    return render(request, 'departmanlar/departman_listesi.html', {'departmanlar': departmanlar})

def departman_detay(request, pk):
    departman = get_object_or_404(Departman, pk=pk)
    satin_almalar = SatinAlma.objects.filter(departman=departman)

    # Filtreler
    urun_id = request.GET.get('urun')
    tedarikci_id = request.GET.get('tedarikci')
    tarih1 = request.GET.get('tarih1')
    tarih2 = request.GET.get('tarih2')

    if urun_id:
        satin_almalar = satin_almalar.filter(urun_id=urun_id)
    if tedarikci_id:
        satin_almalar = satin_almalar.filter(tedarikci_id=tedarikci_id)
    if tarih1:
        satin_almalar = satin_almalar.filter(tarih__gte=tarih1)
    if tarih2:
        satin_almalar = satin_almalar.filter(tarih__lte=tarih2)

    toplam_tutar = sum([s.toplam_tutar for s in satin_almalar])

    urunler = Urun.objects.all()
    tedarikciler = Tedarikci.objects.all()

    return render(request, 'departmanlar/departman_detay.html', {
        'departman': departman,
        'satin_almalar': satin_almalar,
        'toplam_tutar': toplam_tutar,
        'urunler': urunler,
        'tedarikciler': tedarikciler,
        'filtre': {
            'urun': urun_id,
            'tedarikci': tedarikci_id,
            'tarih1': tarih1,
            'tarih2': tarih2,
        }
    })

def departman_ekle(request):
    if request.method == "POST":
        form = DepartmanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departman başarıyla eklendi.')
            return redirect('departmanlar:departman_listesi')
    else:
        form = DepartmanForm()
    return render(request, 'departmanlar/departman_form.html', {'form': form})

def departman_duzenle(request, pk):
    departman = get_object_or_404(Departman, pk=pk)
    if request.method == "POST":
        form = DepartmanForm(request.POST, instance=departman)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departman başarıyla güncellendi.')
            return redirect('departmanlar:departman_listesi')
    else:
        form = DepartmanForm(instance=departman)
    return render(request, 'departmanlar/departman_form.html', {'form': form})

def departman_sil(request, pk):
    departman = get_object_or_404(Departman, pk=pk)
    if request.method == "POST":
        departman.delete()
        messages.success(request, 'Departman başarıyla silindi.')
        return redirect('departmanlar:departman_listesi')
    return render(request, 'departmanlar/departman_sil.html', {'departman': departman})

def departman_excel(request, pk):
    departman = get_object_or_404(Departman, pk=pk)
    satin_almalar = SatinAlma.objects.filter(departman=departman)

    # Filtreler
    urun_id = request.GET.get('urun')
    tedarikci_id = request.GET.get('tedarikci')
    tarih1 = request.GET.get('tarih1')
    tarih2 = request.GET.get('tarih2')

    if urun_id:
        satin_almalar = satin_almalar.filter(urun_id=urun_id)
    if tedarikci_id:
        satin_almalar = satin_almalar.filter(tedarikci_id=tedarikci_id)
    if tarih1:
        satin_almalar = satin_almalar.filter(tarih__gte=tarih1)
    if tarih2:
        satin_almalar = satin_almalar.filter(tarih__lte=tarih2)

    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Başlıklar
    headers = ['Ürün', 'Tedarikçi', 'Tarih', 'Miktar', 'Birim Fiyat', 'KDV', 'Toplam Tutar']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Satırlar
    for row, s in enumerate(satin_almalar, start=1):
        worksheet.write(row, 0, s.urun.ad)
        worksheet.write(row, 1, s.tedarikci.ad)
        worksheet.write(row, 2, s.tarih.strftime('%d.%m.%Y'))
        worksheet.write(row, 3, s.miktar)
        worksheet.write(row, 4, float(s.birim_fiyat))
        worksheet.write(row, 5, f"%{s.kdv.oran}" if s.kdv else '-')
        worksheet.write(row, 6, float(s.toplam_tutar))

    workbook.close()
    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=departman_{departman.id}_satinalma_listesi.xlsx'
    return response

# Geçici olarak boş bırakıldı. Gerektiğinde fonksiyonlar eklenecek. 