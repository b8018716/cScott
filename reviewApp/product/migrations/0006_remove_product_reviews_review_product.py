# Generated by Django 4.0.2 on 2022-03-30 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_reviews_alter_product_productphoto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reviews',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='product.product'),
        ),
    ]