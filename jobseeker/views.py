from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request , "jobseeker/jobseeker_dashboard.html")

def showJobs(request):
    pass

def jobDetail(request , jid):
    pass

def applyJob(request , jid):
    pass

def showApplications(request):
    pass

def appliedJobStatus(request , jid):
    pass






