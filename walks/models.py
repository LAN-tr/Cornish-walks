from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Walk(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()