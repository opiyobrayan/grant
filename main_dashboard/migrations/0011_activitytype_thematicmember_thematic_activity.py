# Generated by Django 4.1.1 on 2022-10-10 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_dashboard', '0010_post_body2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=200, verbose_name='Activity Type')),
            ],
        ),
        migrations.CreateModel(
            name='ThematicMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('position', models.CharField(max_length=200, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Thematic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematic', models.CharField(max_length=200, verbose_name='Name of Thematic')),
                ('members', models.ManyToManyField(to='main_dashboard.thematicmember')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=200, verbose_name='Activity Name')),
                ('venue', models.CharField(max_length=200, verbose_name='Venue')),
                ('activity_id', models.CharField(max_length=200, verbose_name='activity id')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_dashboard.activitytype')),
                ('grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_dashboard.grant')),
                ('thematic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_dashboard.thematic')),
            ],
        ),
    ]
