from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Generation(models.Model):
    generation_name = models.CharField(max_length=128)
    generation_number = models.PositiveSmallIntegerField(unique=True)
    next_generation = models.NullBooleanField()
    available_from = models.DateTimeField()
    available_until = models.DateTimeField()

    def __unicode__(self):
        return self.generation_name



class Painting(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User, null=True)
    published = models.DateTimeField(auto_now=True)
    summary = models.TextField(blank=True)
    image = models.ImageField(upload_to='paintings', blank=True)
    generation = models.ForeignKey(Generation, null=True)
    parents = models.ManyToManyField("self",blank=True, null=True)

    def __unicode__(self):
        return self.title


#g1 = Generation(generation_name = "Gen 0", generation_number = 0, available_from =  datetime.date(2013,10,15),available_until= datetime.date(2013,10,25) )
#g2 = Generation(generation_name = "Gen 2", generation_number = 1, available_from =  datetime.date(2013,10,25),available_until= datetime.date(2013,11,15) )