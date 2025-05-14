from django.db import models

class KDV(models.Model):
    ad = models.CharField(max_length=50, verbose_name="KDV Adı", default="")
    oran = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="KDV Oranı (%)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "KDV"
        verbose_name_plural = "KDV Oranları"
        ordering = ['oran']

    def __str__(self):
        return f"%{self.oran} - {self.ad}" if self.ad else f"%{self.oran}"

class ParaBirimi(models.Model):
    kod = models.CharField(max_length=10, verbose_name="Para Birimi Kodu")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Para Birimi"
        verbose_name_plural = "Para Birimleri"
        ordering = ['kod']

    def __str__(self):
        return self.kod

class Birim(models.Model):
    ad = models.CharField(max_length=20, verbose_name="Birim Adı")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Birim"
        verbose_name_plural = "Birimler"
        ordering = ['ad']

    def __str__(self):
        return self.ad 