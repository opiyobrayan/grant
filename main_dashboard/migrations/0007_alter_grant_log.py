# Generated by Django 4.1.1 on 2022-10-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_dashboard', '0006_alter_grant_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='log',
            field=models.ImageField(upload_to=''),
        ),
    ]
