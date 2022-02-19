# Generated by Django 3.2.6 on 2021-09-09 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original',
            name='product_description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='original',
            name='product_name',
            field=models.CharField(max_length=500, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='print',
            name='print_image',
            field=models.FileField(upload_to='static/uploads'),
        ),
    ]