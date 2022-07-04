from django.contrib import admin

# Register your models here.

from users.models import User_profile

@admin.register(User_profile)

class  PerfilesUsuario(admin.ModelAdmin):
    list_display = ['name','mail', 'pet_name']