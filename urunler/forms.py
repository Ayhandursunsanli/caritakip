from django import forms
from .models import Urun

class UrunForm(forms.ModelForm):
    class Meta:
        model = Urun
        fields = ['ad']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
        } 