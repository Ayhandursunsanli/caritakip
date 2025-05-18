from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import KDV, ParaBirimi, Birim
from .forms import KDVForm, ParaBirimiForm, BirimForm
from django.contrib.auth.decorators import login_required

@login_required
def parametre_listesi(request):
    return render(request, 'parametreler/parametre_listesi.html')

@login_required
def kdv_listesi(request):
    kdvler = KDV.objects.all()
    return render(request, 'parametreler/kdv_listesi.html', {'kdvler': kdvler})

@login_required
def kdv_ekle(request):
    if request.method == "POST":
        form = KDVForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'KDV başarıyla eklendi.')
            return redirect('parametreler:kdv_listesi')
    else:
        form = KDVForm()
    return render(request, 'parametreler/kdv_form.html', {'form': form})

@login_required
def kdv_duzenle(request, pk):
    kdv = get_object_or_404(KDV, pk=pk)
    if request.method == "POST":
        form = KDVForm(request.POST, instance=kdv)
        if form.is_valid():
            form.save()
            messages.success(request, 'KDV başarıyla güncellendi.')
            return redirect('parametreler:kdv_listesi')
    else:
        form = KDVForm(instance=kdv)
    return render(request, 'parametreler/kdv_form.html', {'form': form})

@login_required
def kdv_sil(request, pk):
    kdv = get_object_or_404(KDV, pk=pk)
    if request.method == "POST":
        kdv.delete()
        messages.success(request, 'KDV başarıyla silindi.')
        return redirect('parametreler:kdv_listesi')
    return render(request, 'parametreler/kdv_sil.html', {'kdv': kdv})

@login_required
def para_birimi_listesi(request):
    para_birimleri = ParaBirimi.objects.all()
    return render(request, 'parametreler/para_birimi_listesi.html', {'para_birimleri': para_birimleri})

@login_required
def para_birimi_ekle(request):
    if request.method == "POST":
        form = ParaBirimiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Para Birimi başarıyla eklendi.')
            return redirect('parametreler:para_birimi_listesi')
    else:
        form = ParaBirimiForm()
    return render(request, 'parametreler/para_birimi_form.html', {'form': form})

@login_required
def para_birimi_duzenle(request, pk):
    para_birimi = get_object_or_404(ParaBirimi, pk=pk)
    if request.method == "POST":
        form = ParaBirimiForm(request.POST, instance=para_birimi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Para Birimi başarıyla güncellendi.')
            return redirect('parametreler:para_birimi_listesi')
    else:
        form = ParaBirimiForm(instance=para_birimi)
    return render(request, 'parametreler/para_birimi_form.html', {'form': form})

@login_required
def para_birimi_sil(request, pk):
    para_birimi = get_object_or_404(ParaBirimi, pk=pk)
    if request.method == "POST":
        para_birimi.delete()
        messages.success(request, 'Para Birimi başarıyla silindi.')
        return redirect('parametreler:para_birimi_listesi')
    return render(request, 'parametreler/para_birimi_sil.html', {'para_birimi': para_birimi})

@login_required
def birim_listesi(request):
    birimler = Birim.objects.all()
    return render(request, 'parametreler/birim_listesi.html', {'birimler': birimler})

@login_required
def birim_ekle(request):
    if request.method == "POST":
        form = BirimForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Birim başarıyla eklendi.')
            return redirect('parametreler:birim_listesi')
    else:
        form = BirimForm()
    return render(request, 'parametreler/birim_form.html', {'form': form})

@login_required
def birim_duzenle(request, pk):
    birim = get_object_or_404(Birim, pk=pk)
    if request.method == "POST":
        form = BirimForm(request.POST, instance=birim)
        if form.is_valid():
            form.save()
            messages.success(request, 'Birim başarıyla güncellendi.')
            return redirect('parametreler:birim_listesi')
    else:
        form = BirimForm(instance=birim)
    return render(request, 'parametreler/birim_form.html', {'form': form})

@login_required
def birim_sil(request, pk):
    birim = get_object_or_404(Birim, pk=pk)
    if request.method == "POST":
        birim.delete()
        messages.success(request, 'Birim başarıyla silindi.')
        return redirect('parametreler:birim_listesi')
    return render(request, 'parametreler/birim_sil.html', {'birim': birim}) 