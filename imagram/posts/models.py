from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    image = models.ImageField()
    description = models.TextChoices()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created =models.DateTimeField(auto_now_add=True)
    created =models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created =models.DateTimeField(auto_now_add=True)
    created =models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


