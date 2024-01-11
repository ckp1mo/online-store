# Generated by Django 4.2 on 2024-01-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Картинка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
                'permissions': [('set_published', 'Can publish post')],
            },
        ),
    ]
