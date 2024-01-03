from django import forms

from blog.models import BlogRecord
from catalog.forms import StyleFormMixin


class BlogRecordForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = BlogRecord
        fields = ('title', 'body', 'preview',)
