# Generated by Django 2.1.5 on 2019-01-16 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0013_autohelm'),
    ]

    operations = [
        migrations.AddField(
            model_name='autodonor',
            name='helm',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='lk.AutoHelm'),
            preserve_default=False,
        ),
    ]
