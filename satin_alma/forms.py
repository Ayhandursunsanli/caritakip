from django import forms
from .models import SatinAlma

class SatinAlmaForm(forms.ModelForm):
    class Meta:
        model = SatinAlma
        fields = '__all__'
        widgets = {
            'tarih': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        } 