# Generated by Django 4.2.9 on 2024-01-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_remove_movie_category_movie_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.DateField(),
        ),
    ]
