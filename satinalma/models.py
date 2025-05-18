from django.db import models
from tedarikciler.models import Tedarikci
from urunler.models import Urun
from departmanlar.models import Departman
from parametreler.models import KDV, ParaBirimi, Birim

class SatinAlma(models.Model):
    tedarikci = models.ForeignKey(Tedarikci, on_delete=models.CASCADE, verbose_name="Tedarikçi")
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE, verbose_name="Ürün")
    departman = models.ForeignKey(Departman, on_delete=models.SET_NULL, null=True, verbose_name="Departman")
    tarih = models.DateField(verbose_name="Tarih")
    miktar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miktar")
    birim = models.ForeignKey(Birim, on_delete=models.SET_NULL, null=True, verbose_name="Birim")
    birim_fiyat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Birim Fiyat")
    kdv = models.ForeignKey(KDV, on_delete=models.SET_NULL, null=True, verbose_name="KDV")
    para_birimi = models.ForeignKey(ParaBirimi, on_delete=models.SET_NULL, null=True, verbose_name="Para Birimi")
    fis = models.FileField(upload_to='fisler/', blank=True, null=True, verbose_name="Fiş")
    faturaya_baglandi = models.BooleanField(default=False, verbose_name="Faturaya Bağlandı")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Satın Alma"
        verbose_name_plural = "Satın Almalar"
        ordering = ['-tarih']

    def __str__(self):
        return f"{self.tedarikci} - {self.urun} ({self.tarih})"

    @property
    def net_tutar(self):
        return self.miktar * self.birim_fiyat

    @property
    def kdv_tutari(self):
        return self.net_tutar * (self.kdv.oran / 100)

    @property
    def toplam_tutar(self):
        return self.net_tutar + self.kdv_tutari 