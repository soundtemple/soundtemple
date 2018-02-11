from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return 'Tag: %s' % self.title


class Post(models.Model):
    published = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, verbose_name='Tags')

    def __str__(self):
        return 'Post: %s' % self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.CharField(max_length=42)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment: %s' % self.name

    def __unicode__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()
