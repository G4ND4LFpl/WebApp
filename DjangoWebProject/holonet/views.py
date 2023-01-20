from django.shortcuts import render
from datetime import datetime
from django.http import HttpRequest
from .models import Post

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