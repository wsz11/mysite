# Generated by Django 2.1.4 on 2018-12-04 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20181204_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmstring',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_confirmed',
        ),
        migrations.DeleteModel(
            name='ConfirmString',
        ),
    ]
