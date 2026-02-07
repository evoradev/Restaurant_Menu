from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render (request, 'recipes/pages/home.html')

def Contact(request):
    httpResponse = HttpResponse("Contact working!")
    return httpResponse

def About(request):
    httpResponse = HttpResponse("About working!")
    return httpResponse