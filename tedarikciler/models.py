from django.db import models

class Tedarikci(models.Model):
    ad = models.CharField(max_length=255, verbose_name="Firma Adı")
    hizmet = models.CharField(max_length=255, verbose_name="Verdiği Hizmet")
    yetkili = models.CharField(max_length=255, verbose_name="Firma Yetkilisi")
    telefon = models.CharField(max_length=20, verbose_name="Telefon Numarası")
    adres = models.TextField(blank=True, verbose_name="Adres")
    email = models.EmailField(blank=True, verbose_name="E-posta Adresi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tedarikçi"
        verbose_name_plural = "Tedarikçiler"
        ordering = ['ad']

    def __str__(self):
        return self.ad 