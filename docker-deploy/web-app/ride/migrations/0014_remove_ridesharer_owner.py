# Generated by Django 3.0.2 on 2020-02-05 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0013_ridesharer_iscomfirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ridesharer',
            name='owner',
        ),
    ]
