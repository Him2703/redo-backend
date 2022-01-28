# Generated by Django 3.2 on 2022-01-11 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20210905_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('placed', 'PLACED'), ('accepted', 'ACCEPTED'), ('packed', 'PACKED'), ('shipped', 'SHIPPED'), ('delivered', 'DELIVERED')], default='placed', max_length=10),
        ),
    ]