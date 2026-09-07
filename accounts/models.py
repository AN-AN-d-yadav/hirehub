from django.db import models

# Create your models here.

# user ke login information ko store karne 

class AppUser(models.Model):

    GENDER_CHOICES = (('male','Male'),('female','Female'),('others','Others'))
    USER_TYPE = (("recruiter" , "Recruiter") , ("jobseeker" , "Jobseeker"))

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length =255 ,choices=GENDER_CHOICES , default="others" )
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=50)
    u_type = models.CharField(max_length=30 , choices=USER_TYPE , default="jobseeker")
    password = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

# jobseeeker oriented models/ tables 
class Skill(models.Model):
    skill_name = models.CharField(max_length = 255 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill_name

class JobSeeker(models.Model):
    user = models.OneToOneField(AppUser , on_delete=models.CASCADE , related_name="jobseeker")

    # Addresss
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length =255)
    district = models.CharField(max_length=255)
    zip_code = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)

    # skills
    skills = models.ManyToManyField(Skill , related_name="jobseeker")

    # addition details 
    expected_salary = models.IntegerField(null=True , blank = True)
    current_salary = models.IntegerField(null=True , blank = True)
    notice_period = models.IntegerField(null=True , blank = True)
    linkedin_url = models.URLField(null=True , blank = True)
    github_url = models.URLField(null=True , blank = True)
    portfolio_url = models.URLField(null=True , blank = True)
    is_open_to_work = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Education(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE ,related_name="education")
    degree_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    university = models.CharField(max_length = 255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.degree_name} - {self.jobseeker}"

class Experience(models.Model):
    jobseeker = models.ForeignKey(JobSeeker , on_delete = models.CASCADE , related_name="experiences" )
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    start_date = models.PositiveIntegerField()
    end_date = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.company_name}-{self.jobseeker}"

# recruiter oriented models 

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    locality = models.CharField(max_length=255)
    city = models.CharField(max_length =255)
    district = models.CharField(max_length=255)
    zip_code = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)

    logo = models.ImageField(upload_to="company_logo/" , blank=True , null=True)
    website = models.URLField(blank=True , null=True )
    industry = models.CharField(max_length=255 , help_text="Sector")
    established_at = models.PositiveIntegerField()
    details = models.TextField(null=True , blank=True , help_text="Company Description")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.industry}"

class Recruiter(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE , related_name="recruiter")
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name="company" , null=True , blank=True )
    designation = models.CharField(max_length=100)
    craeted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name}-{self.user.last_name}"


    