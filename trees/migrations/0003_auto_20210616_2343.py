# Generated by Django 3.1.4 on 2021-06-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20210616_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='sponsor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='treetype',
            name='company',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='treetype',
            name='latin_name',
            field=models.CharField(max_length=200),
        ),
    ]
