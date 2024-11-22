# Generated by Django 5.0.3 on 2024-11-16 01:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blogs', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_blogs', to='blog.category')),
            ],
        ),
    ]
