# Generated by Django 3.0.5 on 2020-04-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20200415_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='recommend',
            field=models.BooleanField(default=False),
        ),
    ]
