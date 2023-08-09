from django.contrib import admin

# Register your models here.
from .models import Content, Assignment, MyModelAdmin, ModelAdmin


admin.site.register(Content, MyModelAdmin)
admin.site.register(Assignment)