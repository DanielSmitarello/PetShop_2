from django.shortcuts import render
from users.models import User_profile
# Create your views here.

def user_profile(request):
    profile = User_profile.objects.all()
    context = {'profile':profile}
    return render(request,'users/profile.html', context = context)