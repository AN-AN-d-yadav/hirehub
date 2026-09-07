from django.shortcuts import render,redirect
from accounts.models import Skill , AppUser
from . models import JobCategory , Job ,Recruiter
from django.contrib import messages

# Create your views here.

def dashboard(request):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
            messages.error(request , "Login first")
            return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "recruiter":
            messages.error(request , "You are not Authorized to perform this operation")
            return redirect("login")
    
    return render(request , "recruiter/recruiter_dashboard.html")

def postJob(request):
    # who is the user right now
    # koi logged in hai bhi ya nahi 
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    # kon active hai
    user = AppUser.objects.get(id=user_id)
    recruiter  = Recruiter.objects.filter(user = user).first()

    # ek job ko create sirf ek recruiter hi krskta hai 
    if user.u_type != "recruiter":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    
    # saari skills 
    # saari categories
    skills_required = Skill.objects.all()
    job_categories = JobCategory.objects.all()
    context = {
        'skills':skills_required , 
        'categories':job_categories
    }

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description"
        )
        salary = request.POST.get("salary")
        location = request.POST.get("location")
        vacancy = request.POST.get("vacancy")
        deadline = request.POST.get("deadline")
        job_type = request.POST.get("job_type")
        job_category = JobCategory.objects.get(id = request.POST.get("job_category") )   
        skills = request.POST.getlist("skills_required")

        job = Job.objects.create(
            recruiter = recruiter ,
            title = title , 
            description = description , 
            salary = salary , 
            location = location ,
            vacancy = vacancy ,
            deadline = deadline ,
            job_type=job_type,
            category = job_category,
        )
        job.skills_required.set(skills)
        job.save()

        messages.success(request , "job created successfully ")
        return redirect("rec-dashboard")        

    return render(request , "recruiter/create_job.html" , context)

def showjobs(request):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "recruiter":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    recruiter  = Recruiter.objects.get(user = user)
    
    all_jobs = Job.objects.filter(recruiter = recruiter)

    return render(request , "recruiter/show_job.html" , {'jobs':all_jobs})

def jobDetail(request , jid):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "recruiter":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    recruiter  = Recruiter.objects.get(user = user)

    try : 
        job = Job.objects.get(id=jid)
    except:
        messages.error(request , "Job Not Found")
        return redirect("show-job")

    if job.recruiter != recruiter:
        messages.error(request , "Unauthorized Access")
        return redirect("show-job")
    
    return render(request , "recruiter/job_detail.html" , {"job":job})

def updateJobDetail(request , jid):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "recruiter":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    
    recruiter  = Recruiter.objects.get(user = user)

    try:
        job = Job.objects.get(id=jid)
    except:
        messages.error(request , "Job Not Found")
        return redirect("show-job")

    if job.recruiter != recruiter : 
        messages.error(request , "Unauthorized Access ")
        return redirect("show-job")

    skills_required = Skill.objects.all()
    job_categories = JobCategory.objects.all()
    context = {
            'skills':skills_required , 
            'categories':job_categories,
            'job' : job
        }

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description"
        )
        salary = request.POST.get("salary")
        location = request.POST.get("location")
        vacancy = request.POST.get("vacancy")
        deadline = request.POST.get("deadline")
        job_type = request.POST.get("job_type")
        job_category = JobCategory.objects.get(id = request.POST.get("job_category") )   
        skills = request.POST.getlist("skills_required")

        
        job.recruiter = recruiter 
        job.title = title 
        job.description = description  
        job.salary = salary 
        job.location = location 
        job.vacancy = vacancy 
        job.deadline = deadline 
        job.job_type=job_type
        job.category = job_category

        job.skills_required.set(skills)
        job.save()

        messages.success(request , "job updated successfully ")
        return redirect("show-job")

    return render(request , "recruiter/update_job.html" ,context )
    


def deleteJob(request , jid):
    user_id = request.session.get('user_id' , None)
    if user_id is None :
        messages.error(request , "Login first")
        return redirect("login")
    user = AppUser.objects.get(id=user_id)
    if user.u_type != "recruiter":
        messages.error(request , "You are not Authorized to perform this operation")
        return redirect("login")
    
    recruiter  = Recruiter.objects.get(user = user)

    try:
        job = Job.objects.get(id=jid)
    except:
        messages.error(request , "Job Not Found")
        return redirect("show-job")

    if job.recruiter != recruiter : 
        messages.error(request , "Unauthorized Access ")
        return redirect("show-job")
     
    job.delete()
    messages.success(request , "Job Deleted Successfully ")
    return redirect("show-jobs")

    

