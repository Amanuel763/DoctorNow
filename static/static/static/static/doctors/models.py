from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Doc(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    city = models.CharField(max_length=100, default=False)
    state = models.CharField(max_length=100, default=False)
    occupation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    statement = RichTextField(max_length=3000)
    education = RichTextField(max_length=3000)
    address = models.CharField(max_length=250)
    number = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name