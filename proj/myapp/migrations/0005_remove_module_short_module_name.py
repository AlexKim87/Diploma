# Generated by Django 2.2.7 on 2020-02-05 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200205_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='short_module_name',
        ),
    ]