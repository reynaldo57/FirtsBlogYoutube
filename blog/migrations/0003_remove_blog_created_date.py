# Generated by Django 5.0.3 on 2024-11-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_date',
        ),
    ]
