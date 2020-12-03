from django.db import models

# Create your models here.


class Signup(models.Model):
    user_email = models.CharField(max_length=200)
    user_pwd   = models.CharField(max_length=50)
    user_name  = models.CharField(max_length=50)

    def __str__(self):  # localhost:8000/admin에서 나타날문자
        return self.user_name

    class Meta:
        db_table = 'user_db'


class Photo(models.Model):
    post_num   = models.AutoField(unique=True, primary_key=True)
    author     = models.TextField(max_length=50)
    comment    = models.TextField(blank=True)
    image      = models.ImageField(blank= True)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "comment : " + self.comment

    class Meta:
        db_table = 'photo_db'
        ordering = ['-created']


