from django.contrib import admin
from blog.models import BlogRecord


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published',)