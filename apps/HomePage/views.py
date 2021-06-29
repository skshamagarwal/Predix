from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'home_page.html')

def landingPage(request):
    return render(request, 'index.html')