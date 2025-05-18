from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tedarikci
from .forms import TedarikciForm
from satinalma.models import SatinAlma
from faturalar.models import Fatura
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Q
from django.contrib.auth.decorators import login_required

@login_required
def tedarikci_listesi(request):
    # Tedarikçileri ve bakiyelerini al
    tedarikciler = Tedarikci.objects.annotate(
        bakiye=Sum(
            ExpressionWrapper(
                F('satinalma__birim_fiyat') * F('satinalma__miktar') * (1 + (F('satinalma__kdv__oran') / 100.0)),
                output_field=DecimalField()
            ),
            filter=Q(satinalma__faturalari=None)
        )
    ).order_by('ad')
    
    return render(request, 'tedarikciler/tedarikci_listesi.html', {'tedarikciler': tedarikciler})

@login_required
def tedarikci_detay(request, pk):
    tedarikci = get_object_or_404(Tedarikci, pk=pk)
    return render(request, 'tedarikciler/tedarikci_detay.html', {'tedarikci': tedarikci})

@login_required
def tedarikci_ekle(request):
    if request.method == "POST":
        form = TedarikciForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tedarikçi başarıyla eklendi.')
            return redirect('tedarikciler:tedarikci_listesi')
    else:
        form = TedarikciForm()
    return render(request, 'tedarikciler/tedarikci_form.html', {'form': form})

@login_required
def tedarikci_duzenle(request, pk):
    tedarikci = get_object_or_404(Tedarikci, pk=pk)
    if request.method == "POST":
        form = TedarikciForm(request.POST, instance=tedarikci)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tedarikçi başarıyla güncellendi.')
            return redirect('tedarikciler:tedarikci_listesi')
    else:
        form = TedarikciForm(instance=tedarikci)
    return render(request, 'tedarikciler/tedarikci_form.html', {'form': form})

@login_required
def tedarikci_sil(request, pk):
    tedarikci = get_object_or_404(Tedarikci, pk=pk)
    if request.method == "POST":
        tedarikci.delete()
        messages.success(request, 'Tedarikçi başarıyla silindi.')
        return redirect('tedarikciler:tedarikci_listesi')
    return render(request, 'tedarikciler/tedarikci_sil.html', {'tedarikci': tedarikci})

def tedarikci_cari(request, pk):
    tedarikci = get_object_or_404(Tedarikci, pk=pk)
    # Sadece faturasız satın almalar (ödemesi yapılmamışlar)
    satinalmalar = SatinAlma.objects.filter(tedarikci=tedarikci, faturalari=None)
    faturalar = Fatura.objects.filter(tedarikci=tedarikci)
    guncel_bakiye = sum([s.toplam_tutar for s in satinalmalar])
    return render(request, 'tedarikciler/tedarikci_cari.html', {
        'tedarikci': tedarikci,
        'satinalmalar': satinalmalar,
        'faturalar': faturalar,
        'guncel_bakiye': guncel_bakiye,
    }) 