# Generated by Django 4.2.4 on 2024-11-25 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('bs4_inline_alignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inlinealignmentmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin'),
        ),
    ]
