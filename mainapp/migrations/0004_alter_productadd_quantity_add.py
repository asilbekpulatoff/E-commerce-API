# Generated by Django 4.2.7 on 2023-12-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_productadd_quantity_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productadd',
            name='quantity_add',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
