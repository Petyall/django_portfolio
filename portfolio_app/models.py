from django.db import models

# Класс для взаимодействия с БД
class Project(models.Model):
    header = models.CharField(max_length=200, help_text="Заголовок главной страницы")
    header_image = models.ImageField(upload_to='portfolio/images/', help_text="Картинка главной страницы (750x422)")
    title = models.CharField(max_length=100, help_text="Заголовок PopUp окна")
    description = models.TextField(help_text="Описание PopUp окна")
    image = models.ImageField(upload_to='portfolio/images/', help_text="Картинка PopUp окна (900x650)")
    stack = models.CharField(max_length=200, help_text="Стек в PopUp окне")