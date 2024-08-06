from django.db import models


# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    #image = models.ImageField()
    #file = models.FileField()

class car(models.Model):
    name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
    def __str__(self) -> str :
        return self.name
