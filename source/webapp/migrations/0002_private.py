# Generated by Django 2.2 on 2020-03-14 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Private',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_by', to='webapp.File')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Приват',
                'verbose_name_plural': 'Приват',
            },
        ),
    ]
