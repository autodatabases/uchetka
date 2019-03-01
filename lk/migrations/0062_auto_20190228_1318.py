# Generated by Django 2.1.5 on 2019-02-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0061_auto_20190227_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='stocks',
            field=models.ManyToManyField(blank=True, to='lk.Stock'),
        ),
    ]
