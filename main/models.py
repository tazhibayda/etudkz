from django.db import models


# Create your models here.

class Course(models.Model):
    coursename = models.CharField(max_length=256, null=False)
    teacher = models.CharField(max_length=32, null=False)
    # icon = models.ImageField(upload_to='images' , null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

