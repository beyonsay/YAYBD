from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

class Content(models.Model):
    TAGS = (
        ('video', 'Video'),
        ('image', 'Image'),
        ('pdf', 'Pdf'),
    )

    TOPICS = (
        ('Baby Development', 'Baby Development'),
        ('Baby Health', 'Baby Health'),
        ('Parent Health', 'Parent Health'),
    )

    LANG = (
        ('English', 'English'),
        ('IsiXhosa', 'IsiXhosa'),
        ('ChiShona', 'ChiShona'),
        ('Afrikaans', 'Afrikaans'),
    )

    VISIBILITY = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    idContent = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    file = models.FileField()
    visible = models.CharField(max_length=10, choices=VISIBILITY)
    tag = models.CharField(max_length=10, choices=TAGS)
    topics = models.CharField(max_length=30, choices=TOPICS)
    language = models.CharField(max_length=15, choices=LANG)
    assignedUsers = models.ManyToManyField(User, blank=True)

    class Meta:
        db_table = 'Content'

    def __str__(self):
        return self.title

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'tag', 'topics', 'language', 'display_assigned_users']
    search_fields = ('title',)

    list_per_page = 20

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def display_assigned_users(self, obj):
        return ", ".join([user.username for user in obj.assignedUsers.all()])

    display_assigned_users.short_description = 'Assigned Users'

class ModelAdmin(admin.ModelAdmin):
        list_display = ['title', 'visible', 'tag', 'topics', 'language', 'assignedUsers']


