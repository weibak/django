# Generated by Django 4.0.1 on 2022-02-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="text",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
