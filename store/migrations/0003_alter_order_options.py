# Generated by Django 4.1.5 on 2023-01-27 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]