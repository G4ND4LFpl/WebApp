"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views # default


urlpatterns = [
    path('', include("holonet.urls")),
    # Default
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admin-login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='adminlogin'),
    path('admin-logout/', LogoutView.as_view(next_page='/'), name='adminlogout'),
    path('admin/', admin.site.urls)
]
