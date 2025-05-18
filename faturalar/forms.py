from django import forms
from .models import Fatura
from satinalma.models import SatinAlma
from tedarikciler.models import Tedarikci

class FaturaForm(forms.ModelForm):
    satinalmalar = forms.ModelMultipleChoiceField(
        queryset=SatinAlma.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Faturaya Bağlanacak Satın Almalar"
    )
    fatura_dosya = forms.FileField(
        required=True,
        label="Fatura Dosyası",
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    tedarikci = forms.ModelChoiceField(
        queryset=Tedarikci.objects.all(),
        disabled=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        label="Tedarikçi"
    )

    class Meta:
        model = Fatura
        fields = ['tedarikci', 'fatura_no', 'fatura_tarihi', 'odeme_tarihi', 'tutar', 'fatura_dosya', 'satinalmalar']
        widgets = {
            'fatura_tarihi': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'odeme_tarihi': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tutar': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fatura_no': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        tedarikci = kwargs.pop('tedarikci', None)
        super().__init__(*args, **kwargs)
        
        # Set initial values for dates
        if not self.instance.pk:  # Only for new invoices
            from datetime import date
            self.fields['fatura_tarihi'].initial = date.today()
            self.fields['odeme_tarihi'].initial = date.today()
        
        if tedarikci:
            self.fields['satinalmalar'].queryset = SatinAlma.objects.filter(
                tedarikci=tedarikci, 
                faturalari=None
            ).select_related('tedarikci', 'urun')
            self.fields['tedarikci'].initial = tedarikci
            self.fields['tedarikci'].widget.attrs['readonly'] = True
        else:
            self.fields['satinalmalar'].queryset = SatinAlma.objects.filter(
                faturalari=None
            ).select_related('tedarikci', 'urun') 