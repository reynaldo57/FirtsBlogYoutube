# Generated by Django 5.0.3 on 2024-11-20 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='banner',
            field=models.ImageField(null=True, upload_to='blog_banners'),
        ),
        migrations.AddField(
            model_name='blog',
            name='descripcion',
            field=models.CharField(max_length=550, null=True),
        ),
    ]
