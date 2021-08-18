from django.db import models
from django.urls import reverse

from django.db.models.lookups import IntegerLessThan
from django.db.models.query import prefetch_related_objects

# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=200, blank = False,  null = False)
    stack = models.CharField(max_length=200, blank= True, null= True, default='')
    phone_number = models.IntegerField()
    city = models.CharField(max_length=200, blank = False, null = False, default='')
    github = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class School(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField()
    
    def __str__(self):
        return self.name

class SkillSet(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Contact_form(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.email
