from django.contrib import admin
from .models import todo_mod
# Register your models here.

admin.site.register(todo_mod)

#DONT FORGET
# python manage.py makemigrations
# python manage.py migrate
