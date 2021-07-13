from django.shortcuts import render

from .models import Product


# Create your views here.
def home(request):
    items = Product.objects.all()
    return render(request, 'index.html', {'items': items})


def product(request):
    items = Product.objects.all()
    return render(request, 'products.html', {'items': items})


def contact(request):
    return render(request, 'contact.html')
