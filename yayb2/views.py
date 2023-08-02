# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
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
authe = firebase.auth()
database=firebase.database()


# def home(request):
#     day = database.child('logins').child('user1').child('password').get().val()
#     id = database.child('logins').child('user1').child('username').get().val()
#     return render(request,"home.html",{"day":day,"id":id })

def hello_geeks (request) :
	day = database.child('logins').child('user1').child('password').get().val()
	print(day)
	
	return HttpResponse("Hello Geeks")

def main(request):
  # template = loader.get_template('main/main.html')
  # item = Users.objects.get(idUsers=1)
  # allcontent = Content.objects.all()

  allcontent = database.child('logins').child('user1').child('password').get().val()
  # return HttpResponse(template.render())

  return render(request, 'main.html', {'allcontent': allcontent})

def content(request, contentID = None):
  content = None
  if contentID:
    content = get_object_or_404(Content, id=contentID)
  allcontent = Content.objects.all()
  ref = db.reference('/article/-NZLc0JR8XDsC45wFmwd/url')
  data = ref.get()
  print(data)
  return render(request, 'main/content.html', {'content': content, 'allcontent': allcontent, 'data': data})

def logged(request):
  template = loader.get_template('main/logged.html')
  return HttpResponse(template.render())
