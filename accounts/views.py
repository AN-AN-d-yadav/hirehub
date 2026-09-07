from django.shortcuts import render , redirect
from .models import AppUser , JobSeeker , Recruiter
from django.contrib import messages
# Create your views here.

def registerView(request):
    if request.method == "POST":
        gender = request.POST.get("gender")
        u_type = request.POST.get("utype")
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        contact_no = request.POST.get("cno")

        exists = AppUser.objects.filter(email =email ).exists()
        if exists :
            messages.error(request , "Email Already Registered ")
            return redirect("register")
        
        user = AppUser.objects.create(gender=gender ,first_name=f_name , last_name=l_name , email=email , contact_no = contact_no , password = password , u_type=u_type)

        if user.u_type == "jobseeker":
            js = JobSeeker.objects.create(user = user)
            messages.success(request , "User role Updated Successfully ")
            return redirect("login")
        elif user.u_type == "recruiter":
            rec = Recruiter.objects.create(user = user)
            messages.success(request , "User role Updated Successfully ")
            return redirect("login") 

    return render(request , "accounts/register.html")

def loginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")

        # ye email kiska hai ?
        user = AppUser.objects.filter(email = email).first()
        if not user :
             messages.error(request , "user not found ")
             return redirect("login")

        if user.password != password :
            messages.error(request , "Incorrect password")
            return redirect("login")

        # user bhi milgya , aur password bhi match krgya .
        # user ko login krwa do 
        # login krwane ka mtlb hota hai ki server ko ye pehle se  pta ho ki aap kon hai .
        # aur server aapko memorize krne keliye sessions ka use krta hai 
        # sessions basically table hote hai jaha pe server un sabhi logo ke details ko store krta hai jinhone login kiya hota hai .
        
        request.session['user_id'] = user.id
        request.session['email'] = user.email

        messages.success(request , "you are logged in successfully ! ")
        if user.u_type == "jobseeker":
            return redirect("js-dashboard")
        elif user.u_type == "recruiter":
            return redirect("rec-dashboard")

        # return redirect("home")

    return render(request , "accounts/login.html")

def logoutView(request):
    if request.method == "POST":
        request.session.flush()
        return redirect("login")
    
    return redirect("login")