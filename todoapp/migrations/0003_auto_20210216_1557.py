# Generated by Django 3.1.6 on 2021-02-16 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20210216_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['date', '-done']},
        ),
    ]
