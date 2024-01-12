from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, home_page

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home_page, name='home'),
    path('catalog/', ProductListView.as_view(), name='list_product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]
