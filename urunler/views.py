from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Urun
from .forms import UrunForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q

@login_required
def urun_listesi(request):
    urunler = Urun.objects.all()
    return render(request, 'urunler/urun_listesi.html', {'urunler': urunler})

@login_required
def urun_detay(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    return render(request, 'urunler/urun_detay.html', {'urun': urun})

@login_required
def urun_ekle(request):
    if request.method == "POST":
        form = UrunForm(request.POST)
        if form.is_valid():
            # Aynı isimde ürün var mı kontrol et
            urun_adi = form.cleaned_data['ad']
            if Urun.objects.filter(ad__iexact=urun_adi).exists():
                messages.error(request, 'Bu isimde bir ürün zaten mevcut!')
                return render(request, 'urunler/urun_form.html', {
                    'form': form,
                    'mevcut_urunler': Urun.objects.all().order_by('ad')
                })
            
            form.save()
            messages.success(request, 'Ürün başarıyla eklendi.')
            return redirect('urunler:urun_listesi')
    else:
        form = UrunForm()
    
    return render(request, 'urunler/urun_form.html', {
        'form': form,
        'mevcut_urunler': Urun.objects.all().order_by('ad')
    })

@login_required
def urun_duzenle(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    if request.method == "POST":
        form = UrunForm(request.POST, instance=urun)
        if form.is_valid():
            # Aynı isimde başka bir ürün var mı kontrol et
            urun_adi = form.cleaned_data['ad']
            if Urun.objects.filter(ad__iexact=urun_adi).exclude(pk=pk).exists():
                messages.error(request, 'Bu isimde başka bir ürün zaten mevcut!')
                return render(request, 'urunler/urun_form.html', {
                    'form': form,
                    'mevcut_urunler': Urun.objects.all().order_by('ad')
                })
            
            form.save()
            messages.success(request, 'Ürün başarıyla güncellendi.')
            return redirect('urunler:urun_listesi')
    else:
        form = UrunForm(instance=urun)
    
    return render(request, 'urunler/urun_form.html', {
        'form': form,
        'mevcut_urunler': Urun.objects.all().order_by('ad')
    })

@login_required
def urun_sil(request, pk):
    urun = get_object_or_404(Urun, pk=pk)
    if request.method == "POST":
        urun.delete()
        messages.success(request, 'Ürün başarıyla silindi.')
        return redirect('urunler:urun_listesi')
    return render(request, 'urunler/urun_sil.html', {'urun': urun})

@login_required
def search_similar_products(request):
    term = request.GET.get('term', '').strip()
    if len(term) < 2:
        return JsonResponse({'similar_products': []})
    
    similar_products = Urun.objects.filter(
        Q(ad__icontains=term) | Q(ad__startswith=term)
    ).values('ad', 'kategori__ad', 'birim__ad')[:5]
    
    # Verileri düzenle
    products = []
    for product in similar_products:
        products.append({
            'ad': product['ad'],
            'kategori': product['kategori__ad'],
            'birim': product['birim__ad']
        })
    
    return JsonResponse({'similar_products': products}) 