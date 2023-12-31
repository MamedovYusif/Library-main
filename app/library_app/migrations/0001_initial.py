# Generated by Django 4.2.7 on 2023-11-22 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_title', models.CharField(max_length=250, verbose_name='Категория')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=250, verbose_name='Название')),
                ('author', models.CharField(max_length=250, verbose_name='Автор')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library_app.genre')),
            ],
        ),
    ]
