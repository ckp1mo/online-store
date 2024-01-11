from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from blog.apps import BlogConfig
from blog.views import BlogRecordCreateView, BlogRecordListView, BlogRecordDetailView, BlogRecordUpdateView, \
    BlogRecordDeleteView, change_status

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(BlogRecordCreateView.as_view()), name='create_post'),
    path('', BlogRecordListView.as_view(), name='list_post'),
    path('view/<int:pk>/', cache_page(60)(BlogRecordDetailView.as_view()), name='view_post'),
    path('edit/<int:pk>/', BlogRecordUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='delete_post'),
    path('status/<int:pk>/', change_status, name='change_status'),
]