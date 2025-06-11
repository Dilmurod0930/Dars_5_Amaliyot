from django.db import models

# Create your models here.

class Kompyuter(models.Model):
    name = models.CharField("Kompyuter nomi", max_length=100)
    model = models.CharField("Model", max_length=100)
    cpu = models.CharField("Protsessor (CPU)", max_length=100)
    ram = models.IntegerField("RAM (GB)")
    storage = models.CharField("Xotira turi va hajmi", max_length=100)
    screen_size = models.DecimalField("Ekran o‘lchami (dyuym)", max_digits=4, decimal_places=2)
    color = models.CharField("Rangi", max_length=50)
    price = models.DecimalField("Narxi (so‘m)", max_digits=12, decimal_places=2)
    discount_price = models.DecimalField("Chegirma narxi (so‘m)", max_digits=12, decimal_places=2, null=True, blank=True)
    image = models.ImageField("Rasm",upload_to= "kompyuter_App/",  null=True, blank=True)
    description = models.TextField("Tavsif", blank=True, null=True)
    created_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)

    class Meta:
        verbose_name = "Kompyuter"
        ordering = ['-created_at']

    def __str__(self):
        return self.name