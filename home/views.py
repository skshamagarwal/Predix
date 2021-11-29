from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Media, UserMedia
import random
from datetime import date
from home.reccomendation import *


def index(request):
    return render(request, 'index.html')

def dashboard(request, media_type):
    
    # mymovies = list(MyMovies.objects.all().values_list('mid', flat=True))
    # movies = list(Movies.objects.all().filter(mid__isnull=False).filter(cover__isnull=False).exclude(mid__in=mymovies))
    media_list = list(Media.objects.filter(type=media_type))[:20]
    
    # Recommendations
    if request.user.is_authenticated:
        user_movies = UserMedia.objects.all()
        if len(list(user_movies))>1:
            mid_list = []
            for ob in user_movies:
                if ob.mid.type == media_type:
                    mid_list.append(ob.mid.mid)
            recommended = recc(mid_list)
            recommendation = list(Media.objects.filter(mid__in=recommended))
        else:
            recommendation = media_list[:]
    else:
        recommendation = media_list[:]
    
    # Trending List - Current media type and current year, sorted by their ranking(accending)
    trending = list(Media.objects.filter(type=media_type, year=str(date.today().year)).order_by('ranking'))[:20] 
    
    # Latest Releases - Current Year, Sorted by release date (descending)
    latest = list(Media.objects.filter(type=media_type, year=str(date.today().year)).order_by('-rdate'))
    
    # Genre and Language
    genre = media_list[:]
    language = media_list[:]
    
    # Shuffle
    random.shuffle(media_list)
    random.shuffle(genre)
    random.shuffle(language)
    random.shuffle(recommendation)
    
    recommendation_list = recommendation[:20]
    trending_list = trending[:20]
    latest_list = latest[:20]
    genre_list = genre[:50]
    language_list = language[:50]
    
    # Template Object
    obj = {'media_type': media_type.upper(), 'media_list': media_list, 
           "recommendation_list": recommendation_list, "trending_list": trending_list, 
           "latest_list": latest_list, "genre_list":genre_list, "language_list": language_list}
    
    return render(request, 'dashboard.html', obj)


def mediaPage(request, id):
    media_info = Media.objects.filter(mid=id)

    object = {"media_info": media_info[0]}
    return render(request, 'media_page.html', object)


def profile(request, filter):
    mylist = list(UserMedia.objects.filter(uid__id__exact=request.user.id, filter=filter))
    
    object = {'filter': filter, "mylist": mylist}
    return render(request, 'profile.html', object)


# User Add Media
def addMedia(request, mid, to):
    uid = request.user.id
    user_id = User.objects.get(id=uid)
    media = Media.objects.get(mid=mid)
    obj = UserMedia.objects.create(uid=user_id, mid=media, filter=to)
    obj.save()
    return redirect('/')


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