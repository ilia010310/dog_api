# Generated by Django 5.0.6 on 2024-06-12 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='name',
            new_name='name_of_breed',
        ),
    ]
