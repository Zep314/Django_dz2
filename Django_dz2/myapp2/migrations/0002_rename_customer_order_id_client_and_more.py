# Generated by Django 4.2.5 on 2023-09-26 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='id_client',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='id_products',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_ordered',
            new_name='order_date',
        ),
    ]
