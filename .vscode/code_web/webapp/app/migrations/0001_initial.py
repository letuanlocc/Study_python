# Generated by Django 5.0.12 on 2025-03-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(db_column='ProductID', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='ProductName', max_length=40)),
                ('supplier_id', models.IntegerField(blank=True, db_column='SupplierID', null=True)),
                ('category_id', models.IntegerField(blank=True, db_column='CategoryID', null=True)),
                ('quantity_per_unit', models.CharField(blank=True, db_column='QuantityPerUnit', max_length=20, null=True)),
                ('unit_price', models.DecimalField(blank=True, db_column='UnitPrice', decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'Products',
            },
        ),
    ]
