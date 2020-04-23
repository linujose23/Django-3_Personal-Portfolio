from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]
