# Generated by Django 3.1.4 on 2021-01-09 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0013_auto_20210109_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
