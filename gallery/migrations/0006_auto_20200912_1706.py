# Generated by Django 3.0.7 on 2020-09-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20200912_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
