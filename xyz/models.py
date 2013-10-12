from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Generation(models.Model):
    generation_name = models.CharField(max_length=128)
    generation_number = models.PositiveSmallIntegerField(unique=True)
    available_from = models.DateTimeField()
    available_until = models.DateTimeField()

class Painting(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, null=True)
    published = models.DateTimeField(auto_now=True)
    summary = models.TextField(blank=True)
    image = models.ImageField(upload_to='paintings', blank=True)
    generation = models.ForeignKey(Generation, null=True)
    parents = models.ManyToManyField("self",blank=True, null=True)


