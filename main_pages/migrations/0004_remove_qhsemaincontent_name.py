# Generated by Django 5.0.6 on 2024-06-23 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0003_remove_aboutuscontent_related_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qhsemaincontent',
            name='name',
        ),
    ]
