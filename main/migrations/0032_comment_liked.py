# Generated by Django 4.0 on 2022-04-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_course_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
