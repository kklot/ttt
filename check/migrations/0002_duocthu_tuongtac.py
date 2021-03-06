# Generated by Django 3.0.1 on 2020-01-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuocThu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_ngan', models.CharField(max_length=9)),
                ('ten_dai', models.CharField(max_length=200)),
                ('ten_thuongmai', models.CharField(max_length=200)),
                ('nhasanxuat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tuongtac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tt_thuoc_a', models.CharField(choices=[('A', 'thuoc A'), ('B', 'thuoc B'), ('C', 'thuoc C'), ('D', 'thuoc D'), ('E', 'thuoc E'), ('F', 'thuoc F'), ('G', 'thuoc G'), ('H', 'thuoc H'), ('I', 'thuoc I'), ('J', 'thuoc J'), ('K', 'thuoc K'), ('L', 'thuoc L'), ('M', 'thuoc M'), ('N', 'thuoc N'), ('O', 'thuoc O'), ('P', 'thuoc P'), ('Q', 'thuoc Q'), ('R', 'thuoc R'), ('S', 'thuoc S'), ('T', 'thuoc T'), ('U', 'thuoc U'), ('V', 'thuoc V'), ('W', 'thuoc W'), ('X', 'thuoc X'), ('Y', 'thuoc Y'), ('Z', 'thuoc Z')], max_length=200)),
                ('tt_thuoc_b', models.CharField(choices=[('A', 'thuoc A'), ('B', 'thuoc B'), ('C', 'thuoc C'), ('D', 'thuoc D'), ('E', 'thuoc E'), ('F', 'thuoc F'), ('G', 'thuoc G'), ('H', 'thuoc H'), ('I', 'thuoc I'), ('J', 'thuoc J'), ('K', 'thuoc K'), ('L', 'thuoc L'), ('M', 'thuoc M'), ('N', 'thuoc N'), ('O', 'thuoc O'), ('P', 'thuoc P'), ('Q', 'thuoc Q'), ('R', 'thuoc R'), ('S', 'thuoc S'), ('T', 'thuoc T'), ('U', 'thuoc U'), ('V', 'thuoc V'), ('W', 'thuoc W'), ('X', 'thuoc X'), ('Y', 'thuoc Y'), ('Z', 'thuoc Z')], max_length=200)),
                ('tt_hash', models.CharField(max_length=256, unique=True)),
                ('tt_desc', models.TextField()),
                ('tt_rank', models.IntegerField()),
                ('tt_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
