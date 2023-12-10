from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogRecordCreateView, BlogRecordListView, BlogRecordDetailView, BlogRecordUpdateView, \
    BlogRecordDeleteView, change_status

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogRecordCreateView.as_view(), name='create'),
    path('', BlogRecordListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogRecordDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogRecordUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogRecordDeleteView.as_view(), name='delete'),
    path('status/<int:pk>/', change_status, name='change_status'),
]