from django.shortcuts import render
from .models import (Blog)

# Create your views here.

def index (request):
    return render(request, 'index.html')

def blogs (request):
    blogs = Blog.objects.order_by('-created_date')

    context = {
        'blogs':blogs
    }
    return render(request, 'blogs.html', context)