# Generated by Django 4.2.4 on 2024-11-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
