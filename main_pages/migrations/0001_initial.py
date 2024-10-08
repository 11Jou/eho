# Generated by Django 5.0.6 on 2024-06-23 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True)),
                ('title_en', models.CharField(max_length=100)),
                ('content_en', models.TextField(max_length=3000)),
                ('title_ar', models.CharField(max_length=100)),
                ('content_ar', models.TextField(max_length=3000)),
            ],
            options={
                'verbose_name_plural': 'About Us Content',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=100)),
                ('content_en', models.TextField(max_length=3000)),
                ('title_ar', models.CharField(max_length=100)),
                ('content_ar', models.TextField(max_length=3000)),
                ('image', models.FileField(upload_to='Operation Image/%Y/%m/%d/')),
            ],
            options={
                'verbose_name_plural': 'Operation and Service',
            },
        ),
        migrations.CreateModel(
            name='QHSEImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='HSE Image/%Y/%m/%d/')),
            ],
            options={
                'verbose_name_plural': 'QHSE Images',
            },
        ),
        migrations.CreateModel(
            name='QHSEMainContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('title_en', models.CharField(max_length=100)),
                ('content_en', models.TextField(max_length=3000)),
                ('title_ar', models.CharField(max_length=100)),
                ('content_ar', models.TextField(max_length=3000)),
            ],
            options={
                'verbose_name_plural': 'QHSE Main Content',
            },
        ),
        migrations.CreateModel(
            name='QHSEPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='HSE PDF/%Y/%m/%d/')),
            ],
            options={
                'verbose_name_plural': 'QHSE PDF',
            },
        ),
        migrations.CreateModel(
            name='QHSEVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='HSE Video/%Y/%m/%d/')),
            ],
            options={
                'verbose_name_plural': 'QHSE Videos',
            },
        ),
        migrations.CreateModel(
            name='QHSEContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_en', models.TextField(max_length=3000)),
                ('related_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_pages.qhsemaincontent')),
            ],
            options={
                'verbose_name_plural': 'QHSE Content',
            },
        ),
    ]
