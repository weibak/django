# Generated by Django 4.0.1 on 2022-02-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='text',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
