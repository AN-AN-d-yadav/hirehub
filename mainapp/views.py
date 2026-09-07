from django.shortcuts import render , redirect
from accounts.models import AppUser
from django.contrib import messages 
# Create your views here.

def index(request):
    if 'user_id' in request.session :
        user = AppUser.objects.filter(email = request.session['email']).first()
        return render(request , "mainapp/index.html" , {'user':user})
    return render(request , "mainapp/index.html")