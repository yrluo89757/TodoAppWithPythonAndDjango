from django import forms
from .models import ToDoList

class ListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['todo_item', 'completed']
