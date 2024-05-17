from django.db import models
from django.contrib.auth.models import User

# Create your models here and register them in admin.py.

class todo_mod(models.Model): # just like a class
    # model attributes
    user = models.ForeignKey(User, on_delete=models.CASCADE) #<- if user is deleted from db all of its related data will be deleted/cascade 
    todo_name = models.CharField(max_length=1000) #name of task
    status = models.BooleanField(default=False) #status of task

    def __str__(self): # class constructor 
        return self.todo_name