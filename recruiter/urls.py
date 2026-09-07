from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/" , views.dashboard , name="rec-dashboard"),
    path("job/create/" , views.postJob , name="create-job"),
    path("job/show/" , views.showjobs , name="show-job"),
    path("job/show/<int:jid>" , views.jobDetail , name="job-detail"),
]