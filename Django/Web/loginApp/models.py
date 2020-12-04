from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signup(models.Model):
    user_email = models.CharField(max_length=200, unique=True)
    user_pwd   = models.CharField(max_length=50)
    user_name  = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):  # localhost:8000/admin에서 나타날문자
        return self.user_name

    class Meta:
        db_table = 'user_db'




class Photo(models.Model):
    pk_num     = models.AutoField(primary_key=True, unique=True)
    author     = models.CharField(max_length=50)
    comment    = models.TextField(blank=True)
    image      = models.ImageField(blank= True)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "comment : " + self.comment

    class Meta:
        db_table = 'photo_db'
        ordering = ['-created']



class Comment_posting(models.Model):
    post        = models.IntegerField(max_length=50)
    comment_id  = models.CharField(max_length=50)
    comment     = models.TextField(max_length=400)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "comment : " + self.comment_id

    class Meta:
        db_table = 'comment_db'
        ordering = ['created']



