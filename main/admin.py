from django.contrib import admin

# Register your models here.
from .models import Content, MyModelAdmin


admin.site.register(Content, MyModelAdmin)