# Generated by Django 2.0.1 on 2018-03-24 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_20180324_add_user_to_comment_tinymce_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]