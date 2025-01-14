# Generated by Django 4.2.9 on 2024-01-12 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lastName',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_surname',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
