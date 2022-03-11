from django.db import models


# Create your models here.

class Course(models.Model):
    coursename = models.CharField(max_length=256, null=False)
    teacher = models.CharField(max_length=32, null=False)
    # icon = models.ImageField(upload_to='images' , null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.coursename}, Teacher: {self.teacher}, price: {self.price} {self.id}'


class Test(models.Model):
    coursename = models.CharField(max_length=256, null=False)
    teacher = models.CharField(max_length=32, null=False)
    icon = models.ImageField(upload_to='images' )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.coursename}, Teacher: {self.teacher}, price: {self.price} {self.id}'