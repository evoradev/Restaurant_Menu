from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {
        'name': 'Rafael',
        'age': 25,
    }
    return render (request, 'recipes/home.html', context)

def Contact(request):
    httpResponse = HttpResponse("Contact working!")
    return httpResponse

def About(request):
    httpResponse = HttpResponse("About working!")
    return httpResponse