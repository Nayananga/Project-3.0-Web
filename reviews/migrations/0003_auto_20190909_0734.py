# Generated by Django 2.2.1 on 2019-09-09 07:34

from django.db import migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20190830_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='queAndAnsr',
            field=django_mysql.models.JSONField(default=dict),
        ),
    ]