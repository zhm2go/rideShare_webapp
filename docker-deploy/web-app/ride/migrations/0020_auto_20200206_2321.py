# Generated by Django 3.0.2 on 2020-02-06 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ride', '0019_auto_20200206_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ridesharer',
            name='sharer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sharer', to=settings.AUTH_USER_MODEL),
        ),
    ]
