from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Media, UserMedia
import random
from datetime import date
from home.reccomendation import *


def index(request):
    return render(request, 'index.html')

def dashboard(request, media_type):
    
    media_list = list(Media.objects.filter(type=media_type))[:20]
    
    # Recommendations
    try:
        if request.user.is_authenticated:
            user_media = UserMedia.objects.all()
            mid_list = []
            for ob in user_media:
                if ob.mid.type == media_type:
                    mid_list.append(ob.mid.mid)
            if len(mid_list)>1:
                recommended = recc(mid_list, media_type)
                recommendation = list(Media.objects.filter(mid__in=recommended))
            else:
                recommendation = media_list[:]
        else:
            recommendation = media_list[:]
    except Exception as e:
        print(str(e))
    
    # Trending List - Current media type and current year, sorted by their ranking(accending)
    try:
        if media_type=="anime" or media_type=="manga":
            trending = list(Media.objects.filter(type=media_type).order_by('ranking'))[:20] 
        else:
            trending = list(Media.objects.filter(type=media_type, year=str(date.today().year)).order_by('ranking'))[:20] 
    except Exception as e:
        print(str(e))
    
    # Latest Releases - Current Year, Sorted by release date (descending)
    try:
        if media_type=="anime" or media_type=="manga":
            latest = list(Media.objects.filter(type=media_type).order_by('-rdate'))
        else:
            latest = list(Media.objects.filter(type=media_type, year=str(date.today().year)).order_by('-rdate'))
    except Exception as e:
        print(str(e))
    
    # Genre and Language
    genre = media_list[:]
    language = media_list[:]
    
    # Shuffle
    random.shuffle(media_list)
    
    try:
        random.shuffle(recommendation)
        recommendation_list = recommendation[:20]
    except Exception as e:
        recommendation_list = []
    try:
        random.shuffle(trending)
        trending_list = trending[:20]
    except Exception as e:
        trending_list = []
    try:
        random.shuffle(latest)
        latest_list = latest[:20]
    except Exception as e:
        latest_list = []
    try:
        random.shuffle(genre)
        genre_list = genre[:50]
    except Exception as e:
        genre_list = []
    try:
        random.shuffle(language)
        language_list = language[:50]
    except Exception as e:
        language_list = []
        
    
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
def addMedia(request, mid, to, type):
    uid = request.user.id
    user_id = User.objects.get(id=uid)
    media = Media.objects.filter(type=type).get(mid=mid)
    obj = UserMedia.objects.create(uid=user_id, mid=media, filter=to)
    obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# Search Results
def search(request):
    text = request.GET['query']
    if request.user.is_authenticated:
        user_media = UserMedia.objects.all()
        mid_list = []
        for ob in user_media:
            mid_list.append(ob.mid.mid)
        obj = Media.objects.filter(title__icontains=text).exclude(mid__in=mid_list)
    else:
        obj = Media.objects.filter(title__icontains=text)[:50]
    object={'media_list': obj[:100], 'query': text}
    return render(request, 'search.html', object)


# Accounts
def register(request):
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
    else:
        messages.info(request,'Password and Confirm Password is not matching. Try Again')
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        messages.info(request, 'Logged In')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        messages.info(request, 'Invalid Credentials, Try Again')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def logout(request):
    auth.logout(request)
    return redirect('/')