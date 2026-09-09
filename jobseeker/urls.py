from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/" , views.dashboard , name="js-dashboard"),
    path("jobs/" , views.showJobs , name="jobs"),

]