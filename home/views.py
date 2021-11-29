from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Media
import random
from datetime import date


def index(request):
    return render(request, 'index.html')

def dashboard(request, media_type):
    
    # mymovies = list(MyMovies.objects.all().values_list('mid', flat=True))
    # movies = list(Movies.objects.all().filter(mid__isnull=False).filter(cover__isnull=False).exclude(mid__in=mymovies))
    media_list = list(Media.objects.filter(type=media_type))
    
    # Recommendations
    recommendation = media_list[:20]
    
    # Trending List - Current media type and current year, sorted by their ranking(accending)
    trending = list(Media.objects.filter(type=media_type, year=str(date.today().year)).order_by('ranking')) 
    
    # Latest Releases
    latest = list(Media.objects.order_by('-year'))[:20]
    
    # Genre and Language
    genre = media_list[:]
    language = media_list[:]
    
    # Shuffle
    random.shuffle(media_list)
    random.shuffle(genre)
    random.shuffle(language)
    random.shuffle(recommendation)
    
    obj = {'media_type': media_type.upper(), 'media_list': media_list, 
              "recommendation_list": recommendation, "trending_list": trending, 
              "latest_list": latest}
    
    return render(request, 'dashboard.html', obj)

def mediaPage(request, id):
    media_info = Media.objects.filter(mid=id)

    object = {"media_info": media_info[0]}
    return render(request, 'media_page.html', object)

def profile(request):
    object = {}
    return render(request, 'profile.html', object)



# Accounts
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