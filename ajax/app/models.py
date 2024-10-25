# models.py
from django.db import models

class UserApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    experience = models.IntegerField()
    job_role = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username