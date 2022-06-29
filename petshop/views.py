from django.shortcuts import render
from petshop.models import Productos
from petshop.forms import Product_form
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {
    }
    return render(request, 'index.html', context = context)

# def create_product(request):
#     context={}
#     return render(request, 'create_product.html', context=context)

# def create_product_view(request):
#     form = Product_form()
#     context = {'form':form}
#     return render(request, 'create_product.html', context=context)

@login_required
def create_product_view(request):
    if request.method == 'GET':
        form = Product_form()
        context= {'form':form}
        return render(request, 'crud/create_product.html', context=context)
    else:
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Productos.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                is_active = form.cleaned_data['is_active'],

            )
            context = {'new_product':new_product}
            return render(request, 'crud/create_product.html', context=context)

def productos_comida_perro(request):
    comida_perro = Productos.objects.filter(description__icontains='Perro') # modificar para que solo traiga comida de perros
    # comida_perro = Productos.objects.all()
    context = {'comida_perro':comida_perro
               }
    return render(request, 'productos/productos_comida_perro.html',context=context)

def productos_comida_gato(request):
    comida_gato = Productos.objects.filter(description__icontains='gato') # modificar para que solo traiga comida de gatos
    context={'comida_gato':comida_gato
        }
    return render(request, 'productos/productos_comida_gato.html', context=context)

def productos_correa_collar(request):
    collares = Productos.objects.filter(description__icontains='Collar')
    correas = Productos.objects.filter(description__icontains='Correa')# modificar para que solo traiga correas y collares
    context={'correas':correas,
             'collares':collares
    }
    return render(request, 'productos/productos_correa_collar.html', context=context)

def detail_product(request, pk):
    try:
        product = Productos.objects.get(id=pk)
        context={'product':product
        }
        return render(request, 'crud/detail_product.html', context=context)
    except:
        context={'error':'El producto no existe'}
        return render(request, 'crud/detail_product.html',context=context)

@login_required
def delete_product(request, pk):
    try:
        if request.method == 'GET':
            product = Productos.objects.get(id=pk)
            context={'product':product}
            print("1")
        else:
            product = Productos.objects.get(id=pk)
            print(3)
            product.delete()
            print(4)
            context={'message':'Producto eliminado correctamente'}
        return render(request, 'crud/delete_product.html', context=context)
    except:
        print(5)
        context={'error':'El producto que se busca eliminar no existe'}
        return render(request, 'crud/delete_product.html', context=context)

class Update_product(LoginRequiredMixin,UpdateView):
    model = Productos
    template_name = 'crud/update_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('crud/detail_product', kwargs = {'pk':self.object.pk})
