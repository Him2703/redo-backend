# Generated by Django 3.2.8 on 2022-02-26 12:55

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_auto_20220111_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.get_uplaod_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.get_uplaod_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=shop.models.get_uplaod_file_name),
        ),
    ]
