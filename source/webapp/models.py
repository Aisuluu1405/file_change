from django.contrib.auth.models import User
from django.db import models

ACCESS_CHOICES = (
    ('common', 'Общий'),
    ('hidden', 'Скрытый'),
    ('privat', 'Приватный'),
)
class File(models.Model):

    file = models.FileField(upload_to='file_to', verbose_name='Файл')

    name = models.CharField(max_length=100, verbose_name='Название')

    author = models.ForeignKey(User, related_name='file_author', on_delete=models.PROTECT,
                               default=None, null=True, blank=True, verbose_name='Автор')

    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    access = models.CharField(max_length=50, choices=ACCESS_CHOICES, default=ACCESS_CHOICES[0][0],
                                verbose_name='Категория')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'