from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Skill(models.Model) :
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__ (self):
        return (self.title)

class Profile(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)    
    phone = models.CharField(max_length=13, blank=True)
    profile_photo = models.ImageField(upload_to='photos', blank=True)  
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    #override the save method
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Profile, self).save() # Call the "real" save() method.                                          

