# Generated by Django 3.1.4 on 2021-01-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0012_auto_20210109_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firm',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
