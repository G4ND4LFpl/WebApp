from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from . import views,forms

urlpatterns = [
    path('', views.index, name='index'),
    path('create-post/', views.create_post, name='create_post'),
    path('create-comment/', views.create_comment, name='create_comment'),
    path('profile/', views.profile, name='profile'),
    path('sing-in/', views.sing_in, name='sing_in'),
    path('add-user/', views.add_user, name='add_user'),
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
