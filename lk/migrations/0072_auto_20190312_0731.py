# Generated by Django 2.1.5 on 2019-03-12 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0071_auto_20190307_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autodonor',
            name='generation',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='autodonor',
            name='model',
            field=models.CharField(max_length=80),
        ),
    ]
