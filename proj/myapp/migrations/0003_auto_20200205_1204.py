# Generated by Django 2.2.7 on 2020-02-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200205_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='front_panel_module_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
