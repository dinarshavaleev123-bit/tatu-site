from django.shortcuts import render
from .models import TattooWork


def home(request):
    categories = TattooWork.CATEGORY_CHOICES
    works_by_cat = {}
    for code, name in categories:
        works_by_cat[name] = TattooWork.objects.filter(category=code)
    return render(request, 'portfolio/home.html', {'works_by_cat': works_by_cat})


from django.shortcuts import render

# Create your views here.
