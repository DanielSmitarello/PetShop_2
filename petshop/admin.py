from django.contrib import admin
from petshop.models import Productos, Categoria, Oferta
# Register your models here.

@admin.register(Productos)
class petshopAdmin(admin.ModelAdmin):
     list_display = ['name', 'price', 'SKU']

@admin.register(Categoria)
class petshopAdmin2(admin.ModelAdmin):
     list_display = ['name', 'description']


@admin.register(Oferta)
class ControlOferta(admin.ModelAdmin):
     list_display = ['name','description','promo_img']

