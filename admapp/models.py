from django.db import models

# Create your models here.
class Meta:
    db_table= 'faculty'
    db_table= 'student'
    db_table= 'leave'
    db_table= 'assessment'
    db_table= 'attendance'
class faculty(models.Model):
    facid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20)
    mobile=models.IntegerField(max_length=10, null=True, blank=True)
    batchincharge=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10)
    designation=models.CharField(max_length=10, default='Trainer')
    jdate=models.DateField(default='2019-08-01')
    blood=models.CharField(max_length=5,default='o+')

class student(models.Model):
    stid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    admissionno=models.IntegerField(null=True,blank=True)
    admissiondate=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=10,null=True,blank=True)
   
    batch=models.CharField(max_length=10,null=True,blank=True)
    mobile=models.IntegerField(max_length=10, null=True, blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)
    qualification=models.CharField(max_length=10,default='B. Tech')
    blood=models.CharField(max_length=5,default='o+')
    religion=models.CharField(max_length=10,default='Hindu')
    caste=models.CharField(max_length=10,default='')

class leave(models.Model):
    name=models.CharField(max_length=10)
    ltype=models.CharField(max_length=10)
    day=models.CharField(max_length=10)
    date=models.DateField()
    session=models.CharField(max_length=10)
    reason=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    status=models.CharField(max_length=10,default='pending')

class assessment(models.Model):
    name=models.CharField(max_length=10)
    asno=models.CharField(max_length=10)
    date=models.DateField()
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    mark3=models.IntegerField()
    total=models.IntegerField()

class attendance(models.Model):
     name=models.CharField(max_length=10)
     date=models.DateField()
     status1=models.CharField(max_length=10)
     status2=models.CharField(max_length=10)
     status3=models.CharField(max_length=10)
     status4=models.CharField(max_length=10)
