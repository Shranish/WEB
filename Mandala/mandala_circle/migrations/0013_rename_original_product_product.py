# Generated by Django 3.2.6 on 2021-09-12 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0012_customer_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Original_product',
            new_name='Product',
        ),
    ]
