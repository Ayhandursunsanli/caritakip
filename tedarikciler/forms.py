from django import forms
from .models import Tedarikci

class TedarikciForm(forms.ModelForm):
    class Meta:
        model = Tedarikci
        fields = ['ad', 'hizmet', 'yetkili', 'telefon', 'adres', 'email']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'hizmet': forms.TextInput(attrs={'class': 'form-control'}),
            'yetkili': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        } 