from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/" , views.dashboard , name="rec-dashboard"),
    path("job/create/" , views.postJob , name="create-job"),
    path("job/show/" , views.showjobs , name="show-job"),
    path("job/show/<int:jid>" , views.jobDetail , name="job-detail"),
    path("job/edit/<int:jid>" , views.updateJobDetail , name="job-update"),
    path("job/delete/<int:jid>" , views.deleteJob , name="job-delete"),


    path("job/applicants/<int:jid>" , views.showApplicants , name="job-applicants"),
    path("job/applicant/status/<int:aid>" , views.updateApplicationStatus , name="application-status"),

]
