from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    #return HttpResponse("Hello, world. You're at the Holonet page.")
    return render(request, "index.html")