from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)


class BLogPost(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=205, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    publish = models.BooleanField(default=False)
