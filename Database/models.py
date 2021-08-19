from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models.signals import post_save
from django.dispatch import receiver

class EmpModel(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_age=models.CharField(max_length=100)
    emp_dept=models.CharField(max_length=100)
    emp_email=models.CharField(max_length=100)
    emp_gender=models.CharField(max_length=100)
    emp_salary=models.CharField(max_length=100)
    class Meta:
        db_table="employee"


class Empdept(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_hod=models.CharField(max_length=100)
    class Meta:
        db_table="department"
