from django.db import models
# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class EmployeeInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=16)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    interests = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    school = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    level = models.IntegerField()
    deposit = models.IntegerField()
    credit_number = models.CharField(max_length=64)
    credit_limit = models.IntegerField()
    available_credit = models.IntegerField()
    employment_date = models.DateTimeField(max_length=64, auto_now_add=True)


class Notes(models.Model):
    who = models.CharField(max_length=16)
    wheere = models.CharField(max_length=32)
    contents = models.CharField(max_length=64)
    wheen = models.DateTimeField(max_length=64, auto_now_add=True)
