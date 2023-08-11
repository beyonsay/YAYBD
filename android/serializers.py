from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Content

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'  # This includes all fields from the Content model

# class ContentSerializer(serializers.ModelSerializer):
#     file_url = serializers.SerializerMethodField()

#     class Meta:
#         model = Content
#         fields = ['idContent', 'title', 'tag', 'topics','visible', 'file', 'file_url']  # Add 'file_url' field

#     def get_file_url(self, obj):
#         request = self.context.get('request')
#         if obj.visible == "public":
#             return request.build_absolute_uri(obj.file.url)
#         return None