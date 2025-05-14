from django.db import models
from tedarikciler.models import Tedarikci
from satin_alma.models import SatinAlma

class Fatura(models.Model):
    tedarikci = models.ForeignKey(Tedarikci, on_delete=models.CASCADE, related_name='faturalari')
    fatura_no = models.CharField(max_length=50, verbose_name="Fatura No")
    fatura_tarihi = models.DateField(verbose_name="Fatura Tarihi")
    odeme_tarihi = models.DateField(verbose_name="Ödeme Tarihi")
    tutar = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Tutar")
    fatura_dosya = models.FileField(upload_to='faturalar/', blank=True, null=True, verbose_name="Fatura Dosyası")
    satinalmalar = models.ManyToManyField('satin_alma.SatinAlma', related_name='faturalari', blank=True, verbose_name="Satın Almalar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturalar"
        ordering = ['-fatura_tarihi']

    def __str__(self):
        return f"{self.fatura_no} - {self.tedarikci.ad}" 