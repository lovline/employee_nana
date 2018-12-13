from django.db import models
# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class EmployeeInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(max_length=16)
    gender = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=64)
    school = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    employment_date = models.DateTimeField(max_length=64, auto_now_add=True)
