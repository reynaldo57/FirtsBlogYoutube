from .models import Category

def get_all_categories(reuest):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return context