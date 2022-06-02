from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='FreePost', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment