from django.db import models

# Create your models here.

class Productos(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField()
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='petshop', null=True)
    producto_img = models.ImageField(upload_to='producto_img', null=True, blank=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

#ofertas index
class Oferta(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200,blank = True, null=True)
    promo_img = models.ImageField(upload_to='promo_image', null = True, blank=True)


    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return self.name