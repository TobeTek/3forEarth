# Generated by Django 3.1.4 on 2021-06-23 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0007_tree_planted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tree',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='longtitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
