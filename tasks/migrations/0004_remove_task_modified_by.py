# Generated by Django 3.0.8 on 2020-07-29 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200729_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='modified_by',
        ),
    ]
