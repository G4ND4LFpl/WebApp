from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    user_name = models.CharField(unique=True,max_length=20)
    join_date = models.DateTimeField(default=datetime.now)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.user_name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)