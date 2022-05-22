
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=255,null=True)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.username

class Parent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=200,null=True)
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    sid=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.username

class Faculty(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=200,null=True)
    fname=models.CharField(max_length=200,null=True)
    lname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.username

class Course(models.Model):
    cid=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)
    depcode=models.CharField(max_length=200,null=True)
    sem=models.CharField(max_length=200,null=True)
    faculty=models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.cid

class Department(models.Model):
    deptcode=models.CharField(max_length=200,null=True)
    deptname=models.CharField(max_length=200,null=True)
        
    def __str__(self):
        return self.deptcode

class Program_Outcome(models.Model):
    po_no=models.CharField(max_length=255,null=True,blank=True)
    desc=models.TextField()
    def __str__(self):
        return self.po_no

class Program_Specific_Outcome(models.Model):
    pso_no=models.CharField(max_length=255,null=True,blank=True)
    desc=models.TextField()
        
    def __str__(self):
        return self.pso_no

class Program_Educational_Outcome(models.Model):
    peo_no=models.CharField(max_length=255,null=True,blank=True)
    desc=models.TextField()
        
    def __str__(self):
        return self.peo_no


class Course_Outcome(models.Model):
    co_no=models.CharField(max_length=200,null=True)
    desc=models.TextField()
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.co_no


