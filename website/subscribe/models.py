from django.db import models


# Create your models here.
NEWSLETTER_OPTION = [
    ('W','Weekly'),
    ('M','Monthly')
]

class Subscribs(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION, default='M')


    def __str__(self):
        return self.email

