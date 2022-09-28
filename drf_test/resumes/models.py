from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Resume(models.Model):
    status = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    speciality = models.CharField(max_length=60)
    salary = models.IntegerField()
    education = models.CharField(max_length=60)
    experience = models.TextField(blank=True)
    portfolio = models.CharField(max_length=100)
    title = models.CharField(max_length=70)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    owner = models.ForeignKey(
        User, related_name='resumes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
