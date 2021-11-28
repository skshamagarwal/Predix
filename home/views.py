from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Media
import random


def index(request):
    return render(request, 'index.html')

def dashboard(request, media_type):
    
    # Recommendations
    
    # Media
    media_list = list(Media.objects.all())    
    random.shuffle(media_list)
    
    obj = {'media_type': media_type.upper(), 'media_list': media_list, 
              "recommendation_list": media_list, "trending_list": media_list, 
              "latest_list": media_list, "upcoming_list": media_list}
    
    return render(request, 'dashboard.html', obj)

def mediaPage(request, id):
    media_info = Media.objects.filter(mid=id)

    object = {"media_info": media_info[0]}
    return render(request, 'media_page.html', object)

def profile(request):
    object = {}
    return render(request, 'profile.html', object)

def register(request):
    
    # Change Redirects and messages - pending
    
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    idx = email.index('@')
    username = email[:idx]
    
    if password1==password2:
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already in Use.')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            messages.info(request, 'User Created')
        
    else:
        messages.info(request,'Password and Confirm Password is not matching.')
        return redirect('/')
    return redirect('/')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        messages.info(request, 'Logged In')
        return redirect('/')
    else:
        messages.info(request, 'Invalid Credentials')
        return redirect('/')
    # return redirect('/')
    
def logout(request):
    auth.logout(request)
    return redirect('/')