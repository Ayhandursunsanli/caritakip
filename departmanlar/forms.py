from django import forms
from .models import Departman

class DepartmanForm(forms.ModelForm):
    class Meta:
        model = Departman
        fields = ['ad']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
        } 