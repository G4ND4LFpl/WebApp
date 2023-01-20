from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from . import views,forms

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',
         LoginView.as_view
         (
             template_name='login.html',
             authentication_form=forms.HolonetAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
