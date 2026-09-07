from django.contrib import admin
from .models import AppUser , Skill , JobSeeker,Education,Experience,Recruiter,Company
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Skill)
admin.site.register(JobSeeker)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Recruiter)
admin.site.register(Company)
