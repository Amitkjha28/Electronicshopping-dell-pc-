# Generated by Django 4.0.4 on 2022-04-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_product',
            field=models.BooleanField(default=False),
        ),
    ]
