# Generated by Django 3.0.7 on 2020-09-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20200912_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='mediaName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='media',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]