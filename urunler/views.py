from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Urun
from .forms import UrunForm

def urun_listesi(request):
    urunler = Urun.objects.all()
    return render(request, 'urunler/urun_listesi.html', {'urunler': urunler})

def urun_detay(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    return render(request, 'urunler/urun_detay.html', {'urun': urun})

def urun_ekle(request):
    if request.method == "POST":
        form = UrunForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ürün başarıyla eklendi.')
            return redirect('urunler:urun_listesi')
    else:
        form = UrunForm()
    return render(request, 'urunler/urun_form.html', {'form': form})

def urun_duzenle(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    if request.method == "POST":
        form = UrunForm(request.POST, instance=urun)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ürün başarıyla güncellendi.')
            return redirect('urunler:urun_listesi')
    else:
        form = UrunForm(instance=urun)
    return render(request, 'urunler/urun_form.html', {'form': form})

def urun_sil(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    if request.method == "POST":
        urun.delete()
        messages.success(request, 'Ürün başarıyla silindi.')
        return redirect('urunler:urun_listesi')
    return render(request, 'urunler/urun_sil.html', {'urun': urun}) 