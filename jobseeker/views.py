from django.shortcuts import render,redirect
from django.contrib import messages

from accounts.models import AppUser , JobSeeker , Recruiter
from recruiter.models import Job , JobCategory 

# Create your views here.

def dashboard(request):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
            messages.error(request , "Login first")
            return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "jobseeker":
            messages.error(request , "You are not Authorized to perform this operation")
            return redirect("login")
    
    return render(request , "jobseeker/jobseeker_dashboard.html")

def showJobs(request):
    jobs = Job.objects.filter(is_active=True)

    # job deadline cross krgyi ya nahi 
    # calculate date delta 
    # hume sirf vo jobs dikhani hai jisme deadline - current date >= 0 => 14  - 13 => 1  , 14 - 14 = 0 , time delta 

    return render(request , "jobseeker/jobs.html" , {"jobs":jobs})

def jobDetail(request , jid):
    pass

def applyJob(request , jid):
    pass

def showApplications(request):
    pass

def appliedJobStatus(request , jid):
    pass






