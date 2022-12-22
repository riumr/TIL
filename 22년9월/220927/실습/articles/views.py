from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def index(request):
    todo = Todo.objects.all()
    context = {'todo': todo, }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    todo = Todo(content=content, priority=priority,
                deadline=deadline, completed=True)
    todo.save()
    return redirect('articles:index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('articles:index')
