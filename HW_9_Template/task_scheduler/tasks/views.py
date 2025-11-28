from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm 

def task_list(request):
    tasks = Task.objects.all()
    categories = {}

    
    for task in tasks:
        if task.category not in categories:
            categories[task.category] = []
        categories[task.category].append(task)

    return render(request, 'tasks/task_list.html', {'categories': categories, 'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
