from django.db import models


# Create your models here.


class Guest(models.Model):
    name = models.CharField(max_length=128,default='')
    # code = models.CharField(max_length=128,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    date = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=128,default='')
    STATUSCHOICES = (('G','Going'), ( 'N','Not going'))
    status = models.CharField(max_length=1, choices=STATUSCHOICES, null=True, blank=False, default='Unspecified')

    def __str__(self):
        return self.name
