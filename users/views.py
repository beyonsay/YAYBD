from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def assigned(request): 
    return render(request, 'users/assigned.html')