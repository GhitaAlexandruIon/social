from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('post', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/(<username>)', views.UserPost.as_view(), name='for_user'),
    # path(r'by/(?P<username>[-\W]+)/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='single'),
    path('by/<username>/<pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/(<pk>)', views.DeletePost.as_view(), name='delete'),
]
