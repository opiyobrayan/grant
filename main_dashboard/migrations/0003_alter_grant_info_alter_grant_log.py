# Generated by Django 4.1.1 on 2022-10-03 04:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_dashboard', '0002_alter_grant_currency_alter_grant_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grant',
            name='log',
            field=models.ImageField(default='kelin.png', upload_to=''),
        ),
    ]
