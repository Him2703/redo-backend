# Generated by Django 3.2.4 on 2022-02-12 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_merge_0014_auto_20220124_1838_0015_auto_20220119_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='contact_number',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]