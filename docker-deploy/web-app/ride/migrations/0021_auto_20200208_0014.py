# Generated by Django 3.0.3 on 2020-02-08 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0020_auto_20200206_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='vehicletype',
        ),
        migrations.AddField(
            model_name='ride',
            name='vehicleType',
            field=models.CharField(choices=[('micro', 'micro'), ('SUV', 'SUV'), ('VAN', 'VAN'), ('sedan', 'sedan'), ('CUV', 'CUV')], default='sedan', max_length=16),
        ),
        migrations.AlterField(
            model_name='ride',
            name='isShare',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ride',
            name='special',
            field=models.TextField(default=None, max_length=1000, null=True),
        ),
    ]
