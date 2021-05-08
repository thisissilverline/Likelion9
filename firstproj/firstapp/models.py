from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()


class Eumdong(models.Model):
    Name = models.CharField(max_length=10)
    Birthday = models.DateField()
    Major = models.CharField(max_length=10)
    First_session = models.CharField(max_length=10)
    Second_session = models.CharField(max_length=10)
    In_Dormitory = models.BooleanField()
    Memo = models.TextField()
