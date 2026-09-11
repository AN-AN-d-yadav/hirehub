from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/" , views.dashboard , name="js-dashboard"),
    path("jobs/" , views.showJobs , name="jobs"),
    path("job/<int:jid>" , views.jobDetail , name="jobs"),
    path("job/apply/<int:jid>" , views.applyJob , name="apply"),

]
