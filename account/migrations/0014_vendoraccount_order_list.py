# Generated by Django 3.2 on 2022-01-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_account_order_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendoraccount',
            name='order_list',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
