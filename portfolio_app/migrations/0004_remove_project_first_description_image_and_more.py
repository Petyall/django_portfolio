# Generated by Django 4.2.1 on 2023-06-27 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_alter_project_options_project_link_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='first_description_image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='second_description_image',
        ),
    ]
