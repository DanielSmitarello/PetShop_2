from django.contrib import admin
from petshop.models import Productos, Categoria
# Register your models here.

@admin.register(Productos)
class petshopAdmin(admin.ModelAdmin):
     list_display = ['name', 'price', 'SKU']

@admin.register(Categoria)
class petshopAdmin2(admin.ModelAdmin):
     list_display = ['name', 'description']
