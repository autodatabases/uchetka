# Generated by Django 2.1.5 on 2019-01-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0012_auto_20190116_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoHelm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
    ]
