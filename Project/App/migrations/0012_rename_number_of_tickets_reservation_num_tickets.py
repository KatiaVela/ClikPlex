# Generated by Django 4.2.9 on 2024-01-31 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='number_of_tickets',
            new_name='num_tickets',
        ),
    ]