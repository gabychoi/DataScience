from django.contrib import admin
from .models import Signup, Photo, Comment_posting

# Register your models here.

admin.site.register(Signup)
admin.site.register(Photo)
admin.site.register(Comment_posting)