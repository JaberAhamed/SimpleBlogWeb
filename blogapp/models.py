from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, help_text='authon name')
    image = models.FileField()
    details = models.TextField(help_text='author details')
    def __str__(self):
        return self.name.username

class catagory (models.Model):
    name = models.CharField(max_length=100, help_text='catagory name')
    def __str__(self):
        return self.name

class articla (models.Model):
    artical_author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, help_text='articla title')
    body = models.TextField()
    image = models.FileField()

    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.title
    def get_artical_url(self):
        return reverse('blog:artcle', kwargs={"id": self.id})

    def get_author_url(self):
        return reverse('blog:author', kwargs={"name":self.artical_author.name.username})


class comment(models.Model):

    post = models.ForeignKey(articla, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    post_comment = models.TextField()

    def __str__(self):
        return  self.post.title
