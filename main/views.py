from django.shortcuts import render

# Create your views here.
# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
import pyrebase

config = {
  "apiKey": "AIzaSyB-3u6A7MrhDxwH4lTXlMWxbPCXeKVApFo",
  "authDomain": "bbp2023-e96dd.firebaseapp.com",
  "databaseURL": "https://bbp2023-e96dd-default-rtdb.firebaseio.com",
  "projectId": "bbp2023-e96dd",
  "storageBucket": "bbp2023-e96dd.appspot.com",
  "messagingSenderId": "277712220475",
  "appId": "1:277712220475:web:fc8cefbd2e748918ca071e",
  "measurementId": "G-F3TE7LZ0X0"
};

firebase=pyrebase.initialize_app(config)
database=firebase.database()

def main(request):
  allcontent = database.child('content').get()

  permission = ""
  array = []
  for item in allcontent.each():
    permission = database.child('assignments').child(item.key()).child('userID').get().val()

    contentInfo = {'url': '', 'topics': '', 'tags':'', 'title': '', 'id': ''}

    if permission == "everyone":
      contentInfo['url'] = database.child('content').child(item.key()).child('fileURL').get().val()
      contentInfo['topics'] = database.child('content').child(item.key()).child('topics').get().val()
      contentInfo['tags'] = database.child('content').child(item.key()).child('tags').get().val()
      contentInfo['title'] = database.child('content').child(item.key()).child('title').get().val()
      contentInfo['id'] = item.key()
      
      array.append(contentInfo)
  return render(request, 'main/main.html', {'allcontent': array})

def content(request, contentID):
  url = database.child('content').child(contentID).child('fileURL').get().val()
  topics = database.child('content').child(contentID).child('topics').get().val()
  tags = database.child('content').child(contentID).child('tags').get().val()
  title = database.child('content').child(contentID).child('title').get().val()

  permission = database.child('assignments').child(contentID).child('userID').get().val()
  return render(request, 'main/content.html', {'url': url, 'topics': topics, 'tags': tags, 'title': title, 'permission': permission})

def get_content_by_category(request):
    # if request.method == 'GET':
    #   topic = request.GET.get('topic')
    #   # content = Content.objects.filter(category_id=category_id).values('title', 'body')
    #   # return JsonResponse(list(content), safe=False)
      allcontent = database.child('content').get()
      permission = ""
      array = []
      for item in allcontent.each():
        permission = database.child('assignments').child(item.key()).child('userID').get().val()

        contentInfo = {'url': '', 'topics': '', 'tags':'', 'title': '', 'id': ''}
        topics =  database.child('content').child(item.key()).child('topics').get().val()

        if permission == "everyone" and topic in topics:
          contentInfo['url'] = database.child('content').child(item.key()).child('fileURL').get().val()
          contentInfo['topics'] = database.child('content').child(item.key()).child('topics').get().val()
          contentInfo['tags'] = database.child('content').child(item.key()).child('tags').get().val()
          contentInfo['title'] = database.child('content').child(item.key()).child('title').get().val()
          contentInfo['id'] = item.key()
          
          array.append(contentInfo)

      return JsonResponse(array, safe=False)
      # return render(request, 'main.html', {'allcontent': array})

def category(request, category):
  allcontent = database.child('content').get()  #getting everything from the content "table"
  permission = ""       #will be used to check permissions of a content item
  array = []            #will store all content to be displayed

  for item in allcontent.each():
    permission = database.child('assignments').child(item.key()).child('userID').get().val()

    contentInfo = {'url': '', 'topics': '', 'tags':'', 'title': '', 'id': ''}
    topics =  database.child('content').child(item.key()).child('topics').get().val()

    if permission == "everyone" and category in topics: #if this is an item that everyone can access and is part of the category
      contentInfo['url'] = database.child('content').child(item.key()).child('fileURL').get().val()
      contentInfo['topics'] = database.child('content').child(item.key()).child('topics').get().val()
      contentInfo['tags'] = database.child('content').child(item.key()).child('tags').get().val()
      contentInfo['title'] = database.child('content').child(item.key()).child('title').get().val()
      contentInfo['id'] = item.key()
        
      array.append(contentInfo)

  return render(request, 'main/category.html', {'allcontent': array})

def logged(request):
  template = loader.get_template('main/logged.html')
  return HttpResponse(template.render())

def teesandcees(request):
  template = loader.get_template('main/teesandcees.html')
  return HttpResponse(template.render())
