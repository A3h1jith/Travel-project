from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

class Team(models.Model):
    member = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    jobrole = models.TextField()
    img = models.ImageField(upload_to='teammembers')

    def __str__(self):
        return self.member