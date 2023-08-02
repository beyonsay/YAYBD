"""
URL configuration for yayb2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from yayb2.views import hello_geeks, main, content, logged
from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('get_content', views.get_content_by_category, name='get_content_by_category'),
    path('teesandcees/', views.teesandcees, name='teesandcees'),
    # re_path(r'^(?P<contentID>.+)/$', views.content, name='content'),
    # re_path(r'^(?P<category>.+)/$', views.category, name='category'),
    path('content/<str:contentID>/', views.content, name='content'),
    path('category/<str:category>/', views.category, name='category'),
]
