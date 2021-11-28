from django.shortcuts import render
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