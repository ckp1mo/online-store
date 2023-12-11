from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'


def contacts(request):
    return render(request, 'catalog/contacts.html')
