from django.db import models

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    city = models.CharField(max_length=100, default=False)
    state = models.CharField(max_length=100, default=False)
    occupation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Founder(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    occupation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name