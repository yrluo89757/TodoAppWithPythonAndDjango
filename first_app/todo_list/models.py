from django.db import models

# Create your models here.
class ToDoList(models.Model):
    todo_item = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.todo_item
