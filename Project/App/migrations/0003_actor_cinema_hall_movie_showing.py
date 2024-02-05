# Generated by Django 4.2.9 on 2024-01-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_contact_firstname_remove_contact_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_number', models.IntegerField()),
                ('seat_capacity', models.IntegerField()),
                ('hall_type', models.CharField(max_length=100)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('director', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('poster_image', models.ImageField(upload_to='movies/')),
                ('actors', models.ManyToManyField(to='App.actor')),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cinema')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.movie')),
            ],
        ),
    ]
