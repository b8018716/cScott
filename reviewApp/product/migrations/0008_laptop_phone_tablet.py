# Generated by Django 4.0.2 on 2022-03-31 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_review_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('operatingsystem', models.CharField(max_length=100)),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('dimensions', models.CharField(max_length=100)),
            ],
            bases=('product.product',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.product')),
                ('screensize', models.CharField(max_length=100)),
            ],
            bases=('product.product',),
        ),
    ]
