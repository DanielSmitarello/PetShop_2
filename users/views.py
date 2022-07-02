from django.shortcuts import render, redirect
from users.models import *
from users.forms import  *
from django.views.generic import UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from users.forms import User_registration_form
from django.urls import reverse
from django.http import HttpResponse


# login-logout-registro

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username} a Patitas Petshop'}
                return render (request, 'index.html', context = context)
            else:
                context = {'errors':'usuario no encontrado'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/login.html', context = context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)


def logout_view(request):
    logout(request)
    return redirect ('index')


def register_view(request):
    if request.method =='POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html',context = context)
    else:
        form= User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context = context)

#fin logverse



# inicio profileverse

#get pefil
def user_profile(request):
    try:
        profile = User_profile.objects.get()
        context = {'profile':profile}
        return render(request,'users/profile.html', context = context)
    except:
        context = {'error':'perfil no existe'}
        return render(request, 'index.html',context=context)

#create/update profile
def create_profile(request):
    if request.method == 'GET':
        form = Profile_form()
        context = {'form':form}
        return render(request, 'users/create_profile.html',context)
    else:
        form = Profile_form(request.POST)
        print(request.POST)
        if form.is_valid():
            new_profile = User_profile.objects.create(
                name = form.cleaned_data['name'],
                surname =form.cleaned_data['surname'],
                mail = form.cleaned_data['mail'],
                pet_name= form.cleaned_data['pet_name'],
                #profile_img =form.cleaned_data['profile_img'],
            )
            context = {'new_profile':new_profile}
        return render(request, 'users/create_profile.html',context)

def update_profile(request):
    if request.method == 'GET':
        form = Profile_form()
        context = {'form':form}
        return render(request, 'users/update_profile.html',context)
    else:
        form = Profile_form(request.POST)
        print(request.POST)
        if form.is_valid():
            new_profile = User_profile.objects.update(
                name = form.cleaned_data['name'],
                surname =form.cleaned_data['surname'],
                mail = form.cleaned_data['mail'],
                pet_name= form.cleaned_data['pet_name'],
                #profile_img =form.cleaned_data['profile_img'],
            )
            context = {'new_profile':new_profile}
        return render(request, 'users/update_profile.html',context)

#delete_profile
def delete_profile(request):
    try:
        if request.method == 'GET':
            users = User_profile.objects.get()
            context = {'users':users}
        else:
            users = User_profile.objects.get()
            users.delete()
            context = {'messege':'Perfil eliminado'}

        return render(request, 'users/delete_profile.html', context=context)

    except:
        context = {'error':'el perfil no existe'}
        return render(request, 'index.html',context = context)
#endprofilverse