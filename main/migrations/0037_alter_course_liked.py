# Generated by Django 4.0 on 2022-04-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]