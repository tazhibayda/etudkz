# Generated by Django 4.0 on 2022-04-03 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0025_remove_course_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='added',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
