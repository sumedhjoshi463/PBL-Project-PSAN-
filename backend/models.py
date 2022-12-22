from re import T
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create
#  your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255,)
    body = RichTextField(blank= True, null= True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name=("blog_posts"))

    def total_likes(self):
        return self.likes.count()

    def __str__(self):

        return self.title + '/' + str(self.author)
    def get_absolute_url(self):
    
        return reverse("article-detail", args=(str(self.id)))


 
        
        
        
        
class Category(models.Model):

    name = models.CharField(max_length=255, default='coding')

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        return reverse("home")
