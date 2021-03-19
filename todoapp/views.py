from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from .forms import TaskForm
from .models import Task


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)

    if request.is_ajax():
        tasks = list(Task.objects.values())
        return JsonResponse({'tasks': tasks}, status=200)

    return render(request, 'todo.html')


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.done = True
    task.save()
    return JsonResponse({'task': model_to_dict(task)}, status=200)


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return JsonResponse({'result': 'ok'}, status=200)
