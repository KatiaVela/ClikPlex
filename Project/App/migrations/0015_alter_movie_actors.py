# Generated by Django 4.2.9 on 2024-02-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_showing_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='App.actor'),
        ),
    ]
