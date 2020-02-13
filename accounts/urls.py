from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView, name='login'),
    path(r'logout/', auth_views.LoginView, name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
