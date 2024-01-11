from django.core.management import BaseCommand

from catalog.models import Category


# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         categories_list = [
#             {'name': 'Смартфоны', 'decription': ''},
#             {'name': 'Смарт-часы и браслеты', 'decription': ''},
#             {'name': 'Сотовые телефоны', 'decription': ''},
#         ]
#
#         # for category in categories:
#         #     Category.objects.create(**category)
#
#         Category.objects.all().delete()
#
#         categories_for_create = []
#         for categories_item in categories_list:
#             categories_for_create.append(Category(**categories_item))
#         Category.objects.bulk_create(categories_for_create)
