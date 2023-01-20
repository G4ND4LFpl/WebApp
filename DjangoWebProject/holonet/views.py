from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest
from .models import Post, HolonetUser
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    post_list = Post.objects.order_by('-create_date')[:10]
    params = {
        'title':'Home',
        'year':datetime.now().year,
        'post_list':post_list
        }
    return render(request,'index.html',params)

def profile(request):
    assert isinstance(request, HttpRequest)
    params = {            
        'year':datetime.now().year,
        }
    if request.user.is_authenticated:
        if request.GET.get('user'):
            username = request.GET['user']
            userData = User.objects.get_by_natural_key(username)
        else:
            username=request.user.username
            userData=request.user
        Huser = HolonetUser.objects.get(id = userData.id)
        post_list = Post.objects.filter(author=userData).order_by('-create_date')[:10]
        params.update({
            'title': username,
            'about' : Huser.about,
            'post_list': post_list,
            })
        return render(request,'profile.html',params)
    else:
        params.update({
            'title': 'Sing in',
            })
        return render(request, 'create_profile.html', params)

def create_post(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        if request.POST.get('newpost'):
            newpost_content = request.POST['newpost']
            newpost = Post(author=request.user,content=newpost_content,create_date=datetime.now())
            newpost.save()
    return profile(request)
    