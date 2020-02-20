from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.EpisodeList.as_view(), name='episode_list'),
    path('episodes/<int:pk>', views.EpisodeDetail.as_view(), 
    name='episode_detail'),

    path('comments', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]