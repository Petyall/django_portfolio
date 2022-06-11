from django.contrib import admin
from .models import Project

# Эта строка добавляет проект в админку (все поля наследуются из models.py)
admin.site.register(Project)


