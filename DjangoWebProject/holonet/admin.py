from django.contrib import admin

# Register your models here.
from .models import Post,Comment, HolonetUser

admin.site.register(Post)
admin.site.register(HolonetUser)
admin.site.register(Comment)