# Generated by Django 2.2 on 2020-02-07 02:13

from django.db import migrations, models
from soundtemple.project.storage_backends import PrivateMediaStorage


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(storage=PrivateMediaStorage(), upload_to='')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
