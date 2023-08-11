from django.urls import re_path
from . import views

app_name = 'android'

urlpatterns = [
    re_path('android_login', views.android_login),
    re_path('android_logout', views.android_logout),
    re_path('test_token', views.test_token),
    re_path('get_all_content', views.get_all_content),
]