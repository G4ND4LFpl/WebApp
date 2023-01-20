from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class HolonetUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()

class Post(models.Model):
    author = models.ForeignKey(HolonetUser, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)