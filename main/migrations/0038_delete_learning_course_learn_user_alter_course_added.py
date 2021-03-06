# Generated by Django 4.0.2 on 2022-04-22 11:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0037_alter_course_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Learning',
        ),
        migrations.AddField(
            model_name='course',
            name='learn_user',
            field=models.ManyToManyField(blank=True, related_name='learn_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='added',
            field=models.ManyToManyField(default=None, related_name='added', to=settings.AUTH_USER_MODEL),
        ),
    ]
