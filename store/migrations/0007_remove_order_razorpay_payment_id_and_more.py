# Generated by Django 4.0.5 on 2022-07-05 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_razorpay_order_id_order_razorpay_payment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='razorpay_payment_signature',
        ),
    ]
