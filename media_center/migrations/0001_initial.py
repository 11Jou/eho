# Generated by Django 5.0.6 on 2024-06-23 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='CSR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('title_en', models.CharField(max_length=500)),
                ('content_en', models.TextField(max_length=5000)),
                ('title_ar', models.CharField(max_length=500)),
                ('content_ar', models.TextField(max_length=5000)),
                ('cover', models.ImageField(upload_to='CSR/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'CSR',
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('title_en', models.CharField(max_length=500)),
                ('content_en', models.TextField(max_length=5000)),
                ('title_ar', models.CharField(max_length=500)),
                ('content_ar', models.TextField(max_length=5000)),
                ('cover', models.ImageField(upload_to='events/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('title_en', models.CharField(max_length=500)),
                ('content_en', models.TextField(max_length=5000)),
                ('title_ar', models.CharField(max_length=500)),
                ('content_ar', models.TextField(max_length=5000)),
                ('cover', models.ImageField(upload_to='news/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CSRImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CSR/%Y/%m/%d/')),
                ('related_CSR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_center.csr')),
            ],
            options={
                'verbose_name_plural': 'CSR Images',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('resume', models.FileField(upload_to='resume/%Y/%m/%d/')),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_center.departement')),
            ],
            options={
                'verbose_name_plural': 'Career',
            },
        ),
        migrations.CreateModel(
            name='EventVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='events/%Y/%m/%d/')),
                ('related_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_center.event')),
            ],
            options={
                'verbose_name_plural': 'Events Videos',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d/')),
                ('related_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_center.new')),
            ],
            options={
                'verbose_name_plural': 'News Images',
            },
        ),
    ]
