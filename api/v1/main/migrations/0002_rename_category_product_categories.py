# Generated by Django 5.0.3 on 2024-04-02 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
    ]
