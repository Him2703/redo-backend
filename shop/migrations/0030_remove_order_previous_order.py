# Generated by Django 3.2 on 2022-01-11 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='previous_order',
        ),
    ]
