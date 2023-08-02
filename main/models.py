from django.db import models
import uuid
from django.contrib.auth.models import User

# from firebase_admin import db

# Create your models here.
# class Users(models.Model):
#     USER_TYPES = (
#         ('subscriber', 'Subscriber'),
#         ('administrator', 'Administrator'),
#     )

#     idUsers = models.IntegerField(primary_key=True)
#     userName = models.CharField(max_length=50)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     role = models.CharField(max_length=15, choices=USER_TYPES)

#     class Meta:
#         db_table = 'Users'

class Content(models.Model):
    TAGS = (
        ('video', 'Video'),
        ('image', 'Image'),
        ('pdf', 'Pdf'),
    )

    TOPICS = (
        ('babyDev', 'BabyDev'),
        ('babyHealth', 'BabyHealth'),
        ('parentHealth', 'ParentHealth'),
    )

    LANG = (
        ('english', 'English'),
        ('xhosa', 'Xhosa'),
        ('shona', 'Shona'),
    )

    idContent = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/')
    fileURL = models.CharField(max_length=50)
    tag = models.CharField(max_length=10, choices=TAGS)
    topics = models.CharField(max_length=15, choices=TOPICS)
    language = models.CharField(max_length=8, choices=LANG)

    class Meta:
        db_table = 'Content'

    def __str__(self):
        return self.title

# # class Assignments(models.Model):
# #     Id = models.IntegerField(primary_key=True)
# #     idContent = models.IntegerField()
# #     idUser = models.IntegerField()

# #     class Meta:
# #         db_table = 'Assignments'

class Assignment(models.Model):
    ASSIGNMENT_TYPE_CHOICES = (
        ('Public', 'Public'),
        ('Private', 'Private'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    assignment_type = models.CharField(max_length=10, choices=ASSIGNMENT_TYPE_CHOICES, default='Public')

    class Meta:
        unique_together = ('user', 'content')
        verbose_name_plural = 'Assignments'

    def __str__(self):
        if self.assignment_type == 'Public':
            return f"Public Assignment: {self.idAssign}"
        else:
            return f"{self.user} - {self.idAssign} (Private Assignment)"

