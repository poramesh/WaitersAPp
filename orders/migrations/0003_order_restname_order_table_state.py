# Generated by Django 4.2.1 on 2023-05-10 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_restaddress_remove_order_restname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='RestName',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='Table_state',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]