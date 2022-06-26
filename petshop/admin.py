from django.contrib import admin
from petshop.models import Productos, Categoria
# Register your models here.

admin.site.register(Productos)
# class petshopAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'SKU']

admin.site.register(Categoria)