# Generated by Django 3.2.8 on 2022-05-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_coupons_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupons',
            name='id',
        ),
        migrations.AlterField(
            model_name='coupons',
            name='code',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]