# Generated by Django 5.0.1 on 2024-02-06 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0006_link_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='url',
            new_name='urls',
        ),
    ]
