from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos
               }
    return render(request, 'todo/index.html', context)



@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todo:index')
    else:
        form = TodoForm()

    context = {'form': form}
    return render(request, 'todo/create.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            todo.delete()
            return redirect('todo:index')
    return redirect('todo:index',todo.pk)


def complete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.completed = True
    todo.save()
    return redirect ('todo:index')


def cancel(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.completed = False
    todo.save()
    return redirect ('todo:index')
 