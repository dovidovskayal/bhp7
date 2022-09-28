from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=24, verbose_name='название', help_text='Макс. 24 символа')
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='род. категория')
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='Макс. 140 символов'
    )
    is_published = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('is_published', 'name')


class Product(models.Model):
    title = models.CharField(max_length=36,
                             verbose_name='название',
                             help_text='Макс. 36 символов',
                             null=True,
                             blank=True)
    descr = models.CharField(max_length=140,
                             verbose_name='описание',
                             help_text='Макс. 140 символов',
                             null=True,
                             blank=True)
    article = models.CharField(max_length=16,
                               verbose_name='артикул',
                               help_text='Макс. 16 символов',
                               unique=True)
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')
    price = models.DecimalField(decimal_places=2,
                                max_digits=8,
                                default=0,
                                verbose_name='цена',
                                help_text='Макс. 999999.99',
                                )
    count = models.PositiveSmallIntegerField(default=0,
                                             verbose_name='количество')
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 verbose_name='категория')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             verbose_name='пользователь')
    product = models.ForeignKey('Product',
                                on_delete=models.DO_NOTHING,
                                verbose_name='товар')
    date_created = models.DateTimeField(default=datetime.now,
                                        blank=True,
                                        verbose_name='Дата')
    is_paid = models.BooleanField(default=False,
                                  verbose_name='оплачен')

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'app_orders'
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('date_created', 'is_paid')
