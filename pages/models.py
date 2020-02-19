from django.db import models

from project.storage_backends import PrivateMediaStorage
# import statements are always relative to your manage.py


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class PrivateDocument(models.Model):
    """
    Soundtemple private media files: music and products
    """
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=PrivateMediaStorage())
    name = models.CharField(max_length=250)
