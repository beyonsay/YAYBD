from django.contrib import admin

# Register your models here.
from .models import Content, Assignment

# admin.site.register(Users)
admin.site.register(Content)
admin.site.register(Assignment)