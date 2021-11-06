from django.shortcuts import render

# Create your views here.
def myProfile(request):
    return render(request, 'profile.html')