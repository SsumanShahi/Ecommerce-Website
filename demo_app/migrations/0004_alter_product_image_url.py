# Generated by Django 4.1.7 on 2023-04-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
