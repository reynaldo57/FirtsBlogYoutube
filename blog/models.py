from django.db import models
from user_profile.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Blog(models.Model):

    title = models.CharField(max_length=150, unique=True)
    descripcion = models.CharField (max_length=550,null=True)
    banner = models.ImageField(upload_to='blog_banners', null=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    user = models.ForeignKey(
        User,
        related_name='user_blogs',
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        related_name='category_blogs',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title
    
    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)