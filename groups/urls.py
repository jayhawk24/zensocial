from . import views
from django.urls import path
app_name = 'groups'

urlpatterns = [
    path('', views.ListGroup.as_view(), name='all'),
    path('new', views.CreateGroup.as_view(), name='create'),
    path('post/in/<slug>', views.SingleGroup.as_view(), name='single'),
    path('join/<slug>', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>', views.LeaveGroup.as_view(), name='leave'),
]
