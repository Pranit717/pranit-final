from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class listing(models.Model):
    Title = models.TextField(max_length=5, blank=True)
    property_type = (
                ('Flat','Flat'),
                ('Bungalow','Bungalow'),
                ('PG/Hostel','PG/Hostel'),

    )
    type = models.CharField(max_length=30, blank=True, null= True, choices=property_type)
    property_location = (
                ('Mumbai','Mumbai'),
                ('Pune','Pune'),
                ('Bangalore','Banaglore'),
                ('Hyderabad','Hyderabad'),
                ('Chennai','Chennai'),

    )
    location = models.CharField(max_length=30, blank=True, null= True, choices=property_location)

    property_locality = models.CharField(max_length=20, blank=True)
    icon = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')

    description = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.Title
