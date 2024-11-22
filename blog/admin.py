from django.contrib import admin

# Register your models here.

from .models import *

class AdminBlog(admin.ModelAdmin):
    list_display = ["title", "category", ]

admin.site.register(Blog, AdminBlog)
admin.site.register(Category)