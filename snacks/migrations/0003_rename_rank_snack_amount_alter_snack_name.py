# Generated by Django 4.1.3 on 2022-12-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_snack_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='rank',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='snack',
            name='name',
            field=models.CharField(help_text='the name of snack', max_length=64),
        ),
    ]
