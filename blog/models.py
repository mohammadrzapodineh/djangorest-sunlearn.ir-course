from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=110, verbose_name='article title')
    image = models.ImageField(verbose_name='image of article', upload_to="blog/articles/", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    slug = models.SlugField(blank=True, null=True, verbose_name='slug for Article')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='updated at')
    categories = models.ManyToManyField("Category", verbose_name='categories')
    publisher = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField()
    
    
    def __str__(self):
        return f"Article:{self.title}"
    


class Category(models.Model):
    title = models.CharField(max_length=110)
    
    
    def __str__(self):
        return self.title