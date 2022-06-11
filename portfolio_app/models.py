from django.db import models

# Класс для взаимодействия с БД
class Project(models.Model):
    header = models.CharField(max_length=200, help_text="Заголовок на главной странице")
    header_image = models.ImageField(upload_to='portfolio/images/', help_text="Картинка на главной странице (750x422)")
    first_image_detail = models.ImageField(upload_to='portfolio/images/', help_text="(750x422)")
    first_image_detail_tumb = models.ImageField(upload_to='portfolio/images/', help_text="(750x422)")
    second_image_detail = models.ImageField(upload_to='portfolio/images/', help_text="(750x422)", blank=True)
    second_image_detail_tumb = models.ImageField(upload_to='portfolio/images/', help_text="(750x422)")
    third_image_detail = models.ImageField(upload_to='portfolio/images/', help_text="(750x422)", blank=True)
    third_image_detail_tumb = models.ImageField(upload_to='portfolio/images/', help_text="(750x422)")
    first_description = models.TextField(help_text="Описание проекта")
    first_description_image = models.ImageField(upload_to='portfolio/images/', help_text="Картинка описания проекта (400х400)")
    second_description = models.TextField(help_text="Что сделал ты")
    second_description_image = models.ImageField(upload_to='portfolio/images/', help_text="Картинка действий (400х400)")
    stack = models.CharField(max_length=200, help_text="Стек технологий", blank=True)
    stack_image1 = models.ImageField(upload_to='portfolio/images/', help_text="Картинка стека (400х400)", blank=True)