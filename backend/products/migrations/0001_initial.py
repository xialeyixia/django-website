# Generated by Django 4.2.4 on 2024-12-04 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(null=True, unique=True, verbose_name='ID пользователя')),
                ('user_login', models.CharField(max_length=255, unique=True, verbose_name='Логин')),
                ('user_password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('is_registered', models.BooleanField(default=False, verbose_name='Зарегистрирован')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')),
            ],
            options={
                'verbose_name': 'Телеграмм Пользователь',
                'verbose_name_plural': 'Телеграмм Пользователи',
                'db_table': 'telegram_users',
                'ordering': ['-registered_at'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('description', models.TextField(blank=True, verbose_name='Описание подкатегории')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания подкатегории')),
                ('subcategory_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend_products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'db_table': 'subcategories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='Фотография')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время редактирования')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend_products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]