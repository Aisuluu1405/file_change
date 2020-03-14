# Generated by Django 2.2 on 2020-03-14 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file_to', verbose_name='Файл')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('access', models.CharField(choices=[('common', 'Общий'), ('hidden', 'Скрытый'), ('privat', 'Приватный')], default='common', max_length=50, verbose_name='Категория')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='file_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]