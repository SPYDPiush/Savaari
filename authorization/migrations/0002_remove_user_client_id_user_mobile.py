# Generated by Django 4.0.5 on 2023-05-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='client_id',
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(default=1, max_length=10, unique=True, verbose_name='Mobile No.'),
            preserve_default=False,
        ),
    ]
