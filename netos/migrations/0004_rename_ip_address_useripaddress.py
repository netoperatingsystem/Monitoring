# Generated by Django 3.2 on 2021-06-16 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netos', '0003_ip_address'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IP_Address',
            new_name='Useripaddress',
        ),
    ]
