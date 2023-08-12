from django.shortcuts import render
import os
# Create your views here.
# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Content

def main(request):
  allcontent = Content.objects.filter(visible="public")
  print(allcontent)

  return render(request, 'main/main.html', {'allcontent': allcontent})

def content(request, contentID):

  file = Content.objects.get(idContent=contentID)
  return render(request, 'main/content.html', {'content': file})

def get_content_by_category(request):

  return JsonResponse( safe=False)

def category(request, category):
  allcontent = Content.objects.filter(visible="public").filter(topics=category)

  return render(request, 'main/category.html', {'allcontent': allcontent})

def teesandcees(request):
  template = loader.get_template('main/teesandcees.html')
  return HttpResponse(template.render())
