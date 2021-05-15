from django.db import models

# Create your models here.


class Blog(models.Model):

    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Major = models.CharField(max_length=20)
    In_Dormitory = models.BooleanField()
    MBTI = models.CharField(max_length=10)
    Hobby = models.CharField(max_length=100)
    Nickname = models.CharField(max_length=100)
    Favorite_Food = models.TextField()


class Team(models.Model):

    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Major = models.CharField(max_length=20)
    In_Dormitory = models.BooleanField()
    MBTI = models.CharField(max_length=10)
    Hobby = models.CharField(max_length=100)
    Nickname = models.CharField(max_length=100)
