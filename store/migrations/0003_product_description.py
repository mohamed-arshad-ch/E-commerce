# Generated by Django 3.1 on 2020-09-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='sample description', max_length=250),
            preserve_default=False,
        ),
    ]
