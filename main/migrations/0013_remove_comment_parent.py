# Generated by Django 4.0 on 2022-03-29 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_comment_parent_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]