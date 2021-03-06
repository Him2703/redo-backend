# Generated by Django 3.2 on 2021-09-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20210827_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=170, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
