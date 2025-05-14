from django.db import models

class Departman(models.Model):
    ad = models.CharField(max_length=255, verbose_name="Departman Adı")
    sira = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Departman"
        verbose_name_plural = "Departmanlar"
        ordering = ['ad']

    def __str__(self):
        return self.ad 