from django.conf.urls import url
from django.urls import path, urls

from . import views

app_name = 'posts'

urlpatterns = [
    path('',
         views.PostList.asview(),
         name='all'),
    path('new', views.CreatePost.asview(), name='create'),
    path('by/<username>', views.UserPosts.asview(), name='for_user'),
    path('by/<username>/<int:pk>', views.PostDetail.asview(), name='single'),
    path('delete', views.DeletePost.asview(), name='delete'),
]
