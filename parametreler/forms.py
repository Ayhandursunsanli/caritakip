from django import forms
from .models import KDV, ParaBirimi, Birim

class KDVForm(forms.ModelForm):
    class Meta:
        model = KDV
        fields = ['oran']
        widgets = {
            'oran': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ParaBirimiForm(forms.ModelForm):
    class Meta:
        model = ParaBirimi
        fields = ['kod']
        widgets = {
            'kod': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BirimForm(forms.ModelForm):
    class Meta:
        model = Birim
        fields = ['ad']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
        } 