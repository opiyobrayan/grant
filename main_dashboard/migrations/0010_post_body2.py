# Generated by Django 4.1.1 on 2022-10-07 09:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_dashboard', '0009_alter_grant_info_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
