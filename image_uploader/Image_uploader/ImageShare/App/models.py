from django.db import models

# Create your models here.

class Form(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Images")






# def __str__(self):
#     return self.name