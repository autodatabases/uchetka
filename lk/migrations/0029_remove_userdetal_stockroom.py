# Generated by Django 2.1.5 on 2019-01-30 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0028_remove_stockroom_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetal',
            name='stockroom',
        ),
    ]
