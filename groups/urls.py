from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/<int:pk>/', views.CreateGroup.as_view(), name='create'),
    path('posts/<int:pk>/', views.SingleGroup.as_view(), name='single'),
    path(r'join/(?P<slug>[-\w]+)/$', views.JoinGroup.as_view(), name='join'),
    path(r'leave/(?P<slug>[-\w]+)/$', views.LeaveGroup.as_view(), name='Leave'),
]
