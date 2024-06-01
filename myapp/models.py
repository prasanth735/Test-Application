from django.db import models

# Create your models here.


class Sudent(models.Model):

    name=models.CharField(max_length=200)
    dept=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="student_imges",default="..",null=True)
    admission_no=models.CharField(max_length=150)
    