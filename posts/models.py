from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.text import slugify
from random import randint
import os
# Create your models here.

def split_ext(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_path(instance, filepath):
    name, ext = split_ext(filepath)
    new_name  =  randint(0, 999999999)
    final_path = f"posts/{instance.title}/{instance.id}/{new_name}{ext}"
    return final_path

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    picture = models.ImageField(blank=True, null=True, default=None, upload_to=upload_path)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.utcnow())

    def save(self, *args, **kwargs):
        if self.slug == '':
            new_slug = slugify(self.title)
            if Post.objects.filter(slug=new_slug).exists():
                new_slug = new_slug +'-'+ f'{randint(0,899999999990)}'
            self.slug = new_slug
            super().save()
        if self.picture == '':
            self.picture = None


    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='post_comments')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on post {self.post.title}'