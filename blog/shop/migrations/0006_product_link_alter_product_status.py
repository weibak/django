# Generated by Django 4.0.1 on 2022-02-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_remove_product_text_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[
                    ("FEW", "Small amount"),
                    ("ENOUGH", "Enough good"),
                    ("A_LOT", "A lot of good"),
                ],
                default="IN_STOCK",
                max_length=100,
            ),
        ),
    ]
