# Generated by Django 4.1.7 on 2023-03-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model',
            new_name='Post',
        ),
    ]