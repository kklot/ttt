# Generated by Django 3.0.1 on 2020-01-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_duocthu_tuongtac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuongtac',
            name='tt_hash',
            field=models.CharField(max_length=256),
        ),
    ]
