from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index),
    path('dashboard/<str:media_type>/', home.dashboard, name='dashboard'),
    path('profile/', home.profile, name='profile'),
    # path('media_info/<int:mid>', home.mediaInfo, name='media_info'),
    path('media/<str:id>', home.mediaPage, name='media_page'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
