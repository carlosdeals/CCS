from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='listing'),
    path('<slug:slug>/', views.post_detail, name='view_blog'),
    url(r'^feedback/$', views.feedback, name='feedback'),
]
