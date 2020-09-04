# Generated by Django 2.0.7 on 2020-08-28 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_slug'),
        ('dashboard', '0004_auto_20200828_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]