from django.db import models


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

    def __str__(self):
        return 'Продукт "{name}"'.format(
            name=self.name
        )
