# Generated by Django 4.2 on 2023-05-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_order_payment_method_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_data',
            new_name='order_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Esewa', 'Esewa')], max_length=200, null=True),
        ),
    ]