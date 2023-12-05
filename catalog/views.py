from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наши продукты',
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': product_item.name,
        'description': product_item.description,
        'price': product_item.price,
    }
    return render(request, 'catalog/products.html', context)
