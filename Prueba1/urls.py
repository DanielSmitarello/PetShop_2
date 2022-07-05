"""Prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path, include
from users.views import login_view, logout_view, register_view
from petshop.views import productos_comida_perro, index, create_product_view, productos_comida_gato, productos_correa_collar, detail_product, delete_product, search_product, Update_product # create_product
from users.views import user_profile,delete_profile,create_profile,update_profile
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('search/search_product/', search_product, name= 'search/search_product'),
    path('crud/create_product/', create_product_view, name= 'crud/create_product'),
    path('productos/productos_comida_perro/', productos_comida_perro, name='productos/productos_comida_perro'), # registro view de los productos comida perros
    path('productos/productos_comida_gato/', productos_comida_gato, name='productos/productos_comida_gato' ),
    path('productos/productos_correa_collar/', productos_correa_collar, name='productos/productos_correa_collar'),
    path('crud/detail_product/<int:pk>/', detail_product, name='crud/detail_product'),
    path('crud/delete_product/<int:pk>/', delete_product, name='crud/delete_product'),
    path('crud/update_product/<int:pk>/', Update_product.as_view(), name='crud/update_product'),


    path('auth/login/',login_view, name = 'login'),
    path('auth/logout/',logout_view, name = 'logout'),
    path('auth/register/',register_view, name = 'register'),


    path('users/profile/',user_profile, name = 'profile'),
    path('users/create_profile/',create_profile, name = 'create_profile'),
    path('users/update_profile/',update_profile, name = 'update_profile'),
    path('users/delete_profile/',delete_profile, name = 'delete_profile'),



    # path('petshop/', include('petshop.urls')) # registro de la app
] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)