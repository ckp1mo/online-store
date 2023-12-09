from django.shortcuts import render

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products.html'


def contacts(request):
    return render(request, 'catalog/contacts.html')


# def products(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': product_item.name,
#         'product': product_item,
#     }
#     return render(request, 'catalog/products.html', context)


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Наши продукты',
#     }
#     return render(request, 'catalog/home.html', context)
