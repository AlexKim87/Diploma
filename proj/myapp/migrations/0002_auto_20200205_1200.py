# Generated by Django 2.2.7 on 2020-02-05 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controllermodule',
            name='module',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.Module'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='controller_module',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.ControllerModule'),
        ),
    ]