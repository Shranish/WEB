# Generated by Django 3.2.6 on 2021-09-09 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0005_commissionreq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('product_feedback', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CommissionReq',
        ),
    ]
