# Generated by Django 3.1 on 2020-08-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.TextField(default='Enter text here!', max_length=300)),
            ],
        ),
    ]
