from django.shortcuts import render
from django.contrib import messages
from .models import Content

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def assigned(request):
    user = request.user.id
    allcontent = Content.objects.filter(assignedUsers=user)
    print(allcontent)

    return render(request, 'users/assigned.html',  {'allcontent': allcontent})