# Generated by Django 5.0.1 on 2024-02-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='key',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
