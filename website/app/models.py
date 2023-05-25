from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.text import slugify



# Create your models here.

JOB_TYPE = [('FULL TIME','full_time'),('PART TIME','part_time'),('CONTRACT','contract')]


class Location(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    zip = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.street} {self.city} {self.country} {self.zip}"  

class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class JobPost(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True,max_length=40,unique=True)
    location = models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    skills = models.ManyToManyField(Skills)
    type = models.CharField(max_length=50, choices=JOB_TYPE, default='full_time')


    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args,**kwargs)

    def __str__(self):
        return self.title
