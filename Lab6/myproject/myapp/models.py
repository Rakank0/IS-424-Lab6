from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='students')
    
