from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = ToDoList.objects.all
            messages.success(request, ('Item has been added into the list!'))
            return render(request, "home.html", {'all_items': all_items})
    else:
        all_items = ToDoList.objects.all
        return render(request, "home.html", {'all_items': all_items})

def about(request):
    context = {'name': 'Yirou',
               'hometown': 'Anhui, China',
               'school': 'University of Massachusetts Amherst'}
    return render(request, "about.html", context)

def delete(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')

def cross(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    flag = item.completed
    item.completed = not flag
    item.save()
    return redirect(home)

def edit(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    if request.method == 'POST':
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited!'))
        return redirect(home)
    else:
        return render(request, "edit.html", {'item': item})
