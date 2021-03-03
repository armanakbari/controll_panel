from django.db import models
from django.contrib.auth.models import User
import os
class Responder(models.Model):  #customer
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.username


class Tamrin(models.Model):  # order
    name = models.CharField(max_length=50, null=True)
    question = models.CharField(max_length=1000, null=True)
    deadline_tamrin = models.DateTimeField('date published')
    def __str__(self):
        return self.name

class Answers(models.Model):  #product
    responder = models.ForeignKey(Responder, null=True, on_delete= models.SET_NULL)
    document = models.FileField(upload_to='files/', null=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    tamrin = models.ManyToManyField(Tamrin)
    score = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.document.name

class Vids(models.Model):
    caption = models.CharField(max_length=300)
    video = models.FileField(upload_to='videos')
    upload_time = models.DateTimeField(auto_now_add=True)
    def filename(self):
        return os.path.basename(self.video.name)

    def __str__(self):
        return self.caption


