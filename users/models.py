from django.db import models
from django.contrib.auth.models import User

class Responder(models.Model):  #customer
    username = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.username


class Tamrin(models.Model):  # order
    name = models.CharField(max_length=50, null=True)
    question = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

class Answers(models.Model):  #product
    responder = models.ForeignKey(Responder, null=True, on_delete= models.SET_NULL)
    document = models.FileField(upload_to='medias/files')
    upload_time = models.DateTimeField(auto_now_add=True)
    tamrin = models.ManyToManyField(Tamrin)
    score = models.CharField(max_length=50, null=True)




