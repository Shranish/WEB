# Generated by Django 3.2.6 on 2021-09-14 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0026_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment_method',
        ),
    ]
