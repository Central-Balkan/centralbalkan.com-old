from django.db import models
from django.conf import settings

from central_balkan.common.utils import get_domain


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

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
        domain = get_domain()
        media_url = settings.MEDIA_URL

        return f'{domain}{media_url}{self.image}'

    def __str__(self):
        return 'Продукт "{name}"'.format(
            name=self.name
        )
