# Generated by Django 3.1 on 2020-08-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='user_text',
            field=models.TextField(max_length=100),
        ),
    ]