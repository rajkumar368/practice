from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    clinic_name = models.CharField(max_length=40)

class Clinic_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    clinic_name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=30)


