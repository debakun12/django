from django.db import models
from django.contrib.auth.models import USer
# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text