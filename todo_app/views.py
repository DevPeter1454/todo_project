from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.views.decorators.http import require_POST


def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo_app/index.html', {'todo_items': todo_items})


@require_POST
def add_todo(request):
    title = request.POST['title']
    if title:
        TodoItem.objects.create(title=title)
    return redirect('index')


def complete_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    todo_item.completed = True
    todo_item.save()
    return redirect('index')


def delete_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    todo_item.delete()
    return redirect('index')


def update_todo(request, todo_id):
    todo_item = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        title = request.POST['title']
        todo_item.title = title
        todo_item.save()
        return redirect('index')
    return render(request, 'todo_app/update_todo.html', {'todo_item': todo_item})


def fibonacci(request):
    n = int(request.GET.get('n', 10)) 
    fib_sequence = generate_fibonacci(n)
    return render(request, 'todo_app/fibonacci.html', {'fib_sequence': fib_sequence})


def generate_fibonacci(n):
    if n <= 0:
        return []
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
