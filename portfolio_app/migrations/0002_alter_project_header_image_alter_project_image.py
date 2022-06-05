# Generated by Django 4.0.5 on 2022-06-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='header_image',
            field=models.ImageField(height_field=750, help_text='Картинка главной страницы (750x422)', upload_to='', width_field=422),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(height_field=900, help_text='Картинка PopUp окна (900x650)', upload_to='', width_field=650),
        ),
    ]
