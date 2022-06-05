# Generated by Django 4.0.5 on 2022-06-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_alter_project_header_image_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='header_image',
            field=models.ImageField(help_text='Картинка главной страницы (750x422)', upload_to='portfolio_app/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(help_text='Картинка PopUp окна (900x650)', upload_to='portfolio_app/images/'),
        ),
    ]
