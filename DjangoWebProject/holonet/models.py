from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class HolonetUser(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    about = models.TextField()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=datetime.now)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=datetime.now)