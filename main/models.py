from django.utils import timezone
from django.db import models


# Create your models here.

class Course(models.Model):
    # id = i++
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


class Comment(models.Model):
   author = models.CharField(max_length=64)
   course_id = models.IntegerField(null=False)
   post = models.CharField(max_length=64)
   text = models.TextField(max_length=1024)
   date = models.DateField(default=timezone.now)

   def __str__(self):
       return f'{self.author}, : {self.course_id}, : {self.post} , {self.text} , {self.date} , {self.pk}'