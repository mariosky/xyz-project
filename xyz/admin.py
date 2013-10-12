__author__ = 'mariosky'

from django.contrib import admin
from xyz.models import  Painting, Generation


admin.site.register(Painting)
admin.site.register(Generation)