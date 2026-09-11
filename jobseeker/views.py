from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone

from accounts.models import AppUser , JobSeeker , Recruiter
from recruiter.models import Job , JobCategory , JobApplication

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
    user_id = request.session.get('user_id' , None)
    if user_id is None :
            messages.error(request , "Login first")
            return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "jobseeker":
            messages.error(request , "You are not Authorized to perform this operation")
            return redirect("login")

    jobs = Job.objects.filter(is_active=True , deadline__gte=timezone.now())

    # figure out jobs pe sirf vo jobs dikhe jinme jobseejer -> logged in jobseeker na ho


        

    # job deadline cross krgyi ya nahi 
    # calculate date delta 
    # hume sirf vo jobs dikhani hai jisme deadline - current date >= 0 => 14  - 13 => 1  , 14 - 14 = 0 , time delta 

    # current_time = timezone.now() -> current date and time 
    # deadline = job.deadline
    # delta = deadline - current_time

    # deadline__gte > = timezone.now()

    # deadline     = 10 Sept, 5:00 PM
    # current_time = 10 Sept, 11:00 AM
    # delta = 6:00:00
    # if delta.total_seconds() >= 0:
    # deadline abhi cross nahi hui
    # else:
    # deadline cross ho chuki hai
    return render(request , "jobseeker/jobs.html" , {"jobs":jobs})

def jobDetail(request , jid):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "jobseeker":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    try : 
        job = Job.objects.get(id=jid)

    except:
        messages.error(request , "Job Not Found")
        return redirect("jobs")

    # agar deadline meet hogya hai to simply ya to job send mt kro user ko boldo ki this job is expired 
    # ya to bhejdo aur vha not applicable
    current_time = timezone.now()  
    deadline = job.deadline
    delta = deadline - current_time
    if delta.total_seconds() >= 0:
        # job ka deadline bcha hua hai abhi 
        return render(request , "jobseeker/job_detail.html" , {"job":job})
    
    messages.error(request , "No such Job exist") 
    return redirect("jobs")

def applyJob(request , jid):
    # jobseeker kon hai 
    # job konsi hai 
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "jobseeker":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    jobseeker = JobSeeker.objects.get(user = user)
    try : 
        job = Job.objects.get(id=jid)
    except:
        messages.error(request , "Job Not Found")
        return redirect("jobs")

    exist  = JobApplication.objects.filter(job_id = jid , jobseeker = jobseeker)

    if exist :
        messages.error(request , "You have already applied for this job")
        return redirect("jobs")
    
    application = JobApplication.objects.create(jobseeker=jobseeker , job_id = jid)
    messages.success(request , "Job Applied Successfully ")
    return redirect("jobs")


def showApplications(request):
    pass







# cv upload karana on application
# dont show already applied jobs in show jobs .