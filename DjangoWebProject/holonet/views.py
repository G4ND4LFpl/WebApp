from django.shortcuts import render
from datetime import datetime
from random import randint
from django.http import HttpRequest,HttpResponseRedirect
from .models import Post,Comment, HolonetUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher as Hasher

# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    post_list = Post.objects.order_by('-create_date')[:10]
    comment_dict={}
    for post in post_list:
        comment_list=Comment.objects.filter(post=post).order_by('-create_date')[:5]
        comment_dict.update({post:comment_list})
    params = {
        'title':'Home',
        'year':datetime.now().year,
        'post_list':post_list,
        'comment_dict':comment_dict,
        }
    return render(request,'index.html',params)

def profile(request):
    assert isinstance(request, HttpRequest)
    params = {            
        'year':datetime.now().year,
        }
    if request.GET.get('user'):
        username = request.GET['user']
        userData = User.objects.get_by_natural_key(username)
    elif request.user.is_authenticated:
        username=request.user.username
        userData=request.user
    else:
        return HttpResponseRedirect("/login/")
    Huser = HolonetUser.objects.get(user = userData)
    post_list = Post.objects.filter(author=userData).order_by('-create_date')[:10]
    comment_dict={}
    for post in post_list:
        comment_list=Comment.objects.filter(post=post).order_by('-create_date')[:5]
        comment_dict.update({post:comment_list})
    params.update({
        'title': username,
        'about' : Huser.about,
        'post_list':post_list,
        'comment_dict':comment_dict,
        })
    return render(request,'profile.html',params)

def create_post(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        if request.POST.get('newpost'):
            newpost_content = request.POST['newpost']
            newpost = Post(author=request.user,content=newpost_content,create_date=datetime.now())
            newpost.save()
    return HttpResponseRedirect("/profile/")

def create_comment(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        if request.POST.get('newcomment'):
            newcomment_content = request.POST['newcomment']
            post_id = request.POST['post']
            print(post_id)
            newcomment = Comment(author=request.user,post=Post.objects.get(id=post_id),content=newcomment_content,create_date=datetime.now())
            newcomment.save()
    return HttpResponseRedirect("/")

def sing_in(request):
    params = {            
        'year':datetime.now().year,
        'title': 'Sing in',
        }
    return render(request, 'create_profile.html', params)

def add_user(request):
    assert isinstance(request, HttpRequest)
    if request.method=='POST':
        if check_form_in_request(request):
            post = request.POST
            hasher = Hasher()
            salt = generate_salt()
            hash_password = hasher.encode(post['password'], salt)

            user = User(username = post['username'], password = hash_password)
            user.save()
            holonet_user = HolonetUser(user = user, about = post['about'])
            holonet_user.save()
            return index(request)
    return HttpResponseRedirect("/login/")

def check_form_in_request(request):
    if not request.POST.get('username'): return False
    if not request.POST.get('password'): return False
    if not request.POST.get('password') == request.POST.get('password2'): return False
    return True

def generate_salt() -> str:
    letterrange = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    salt = ""
    for i in range(30):
        salt += letterrange[randint(0, len(letterrange)-1)]
    return salt