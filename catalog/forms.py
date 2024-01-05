from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    bad_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('user',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in self.bad_word:
            raise forms.ValidationError('Недопустимое имя продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data in self.bad_word:
            raise forms.ValidationError('Недопустимое описание продукта')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ModeratorProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)
