# Generated by Django 3.2.8 on 2022-04-17 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_subscribe'),
        ('shop', '0013_auto_20220417_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.address'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='delivery_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.variation'),
        ),
    ]
