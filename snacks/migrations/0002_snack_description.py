# Generated by Django 4.1.3 on 2022-12-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]
