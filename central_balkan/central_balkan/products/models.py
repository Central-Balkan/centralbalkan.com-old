import os
import uuid

from django.db import models
from django.conf import settings

from central_balkan.common.utils import get_domain


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    slug = models.CharField(
        verbose_name='Име за URL',
        max_length=255,
        unique=True
    )

    name = models.CharField(
        verbose_name='Име',
        max_length=255,
        unique=True
    )

    @property
    def products_count(self):
        return self.products.count()

    def __str__(self):
        return 'Категория "{name}"'.format(
            name=self.name
        )


def get_product_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    prefix = 'products'

    return '{}/{}{}'.format(prefix, uuid.uuid4().hex, extension)


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    name = models.CharField(
        verbose_name='Име',
        max_length=255,
    )

    image = models.ImageField(
        'Изображение',
        upload_to=get_product_image_name,
        blank=True,
        null=True
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        to=Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return 'Продукт "{name}"'.format(
            name=self.name
        )
