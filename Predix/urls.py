from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home import views as home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.index),
    path('dashboard/<str:media_type>/', home.dashboard, name='dashboard'),
    path('profile/<str:filter>', home.profile, name='profile'),
    path('media/<str:id>', home.mediaPage, name='media_page'),
    path('add/<str:mid>/<str:to>', home.addMedia, name='addMedia'),
    path('register/', home.register, name='register'),
    path('login/', home.login, name='login'),
    path('logout/', home.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
