# Generated by Django 5.0.1 on 2024-05-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
