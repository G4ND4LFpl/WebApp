from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    post_list = Post.objects.order_by('-create_date')[:10]
    params = {
        'title':'Holonet',
        'year':datetime.now().year,
        'post_list':post_list
        }
    return render(request,'index.html',params)

def profile(request):
    assert isinstance(request, HttpRequest)
    username = request.GET['user']
    userID = User.objects.get_by_natural_key(username)
    post_list = Post.objects.filter(author=userID).order_by('-create_date')[:10]
    params = {
        'title':'Holonet',
        'year':datetime.now().year,
        'post_list':post_list,
        'username':username
        }
    return render(request,'profile.html',params)