from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return 'Tag: %s' % self.title


class Post(models.Model):
    published = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, verbose_name='Tags')

    def __str__(self):
        return 'Post: %s' % self.title


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment: %s' % self.name

    def __unicode__(self):
        return self.text