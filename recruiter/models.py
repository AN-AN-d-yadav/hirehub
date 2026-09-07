from django.db import models
from accounts.models import Recruiter, Skill

# Create your models here.

class JobCategory(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('full_time' , 'Full Time'),
        ('part_time' , 'Part Time'),
        ('internship' , 'Internship'),
        ('contract' , 'Contract')
    )
    job_type = models.CharField(max_length=100 , choices=JOB_TYPE_CHOICES , default='part_time')
    recruiter = models.ForeignKey(Recruiter , on_delete=models.CASCADE , related_name="jobs")
    category = models.ForeignKey(JobCategory , on_delete=models.CASCADE , related_name="jobs")
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.PositiveIntegerField(default=0)
    location = models.TextField()
    vacancy = models.PositiveIntegerField()
    deadline = models.DateTimeField(null=True , blank=True)
    is_active = models.BooleanField(default=True)
    skills_required = models.ManyToManyField(Skill , related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title





