from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за штуку')
    is_published = models.BooleanField(default=True, verbose_name='Статус продукта')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_published',
                'Can publish product'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.SmallIntegerField(default=0, verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус версии')

    def __str__(self):
        return f"{self.product}: {self.version_name}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
