from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from . import forms
from . import models

# Criar Tarefa
@login_required
def taskNew(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            messages.info(request,"Tarefa Criada com Sucesso")
            return redirect("/")
    # GET...
    else:
        form = forms.TaskForm()
        return render(request, 'tasks/add.html', {'form':form})

# Listar Tarefas:
@login_required
def taskList(request):
    search = request.GET.get('search')

    if search:
        tasks = models.Task.objects.filter(title__icontains = search, user = request.user)

    else:
        tasks_list = models.Task.objects.all().order_by('-create_at').filter(user = request.user)

        paginator = Paginator(tasks_list, 5)
        page = request.GET.get('page')

        tasks = paginator.get_page(page) 

    return render(request, 'tasks/list.html', {'tasks' : tasks})

# Visualizar Detalhes da Tarefa:
@login_required
def taskView(request, id):
    task = models.Task.objects.get(pk=id)
    return render(request, 'tasks/task.html', {'task':task})

# Editar Tarefas:
@login_required
def taskEdit(request, id):
    task = get_object_or_404(models.Task, pk=id)
    form = forms.TaskForm(instance=task)

    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            messages.info(request, "Tarefa Editada com Sucesso")
            return redirect("/")
            
        else:
            return render(request, 'tasks/edit.html', {'form':form, 'task':task})
    
    else:
        return render(request, 'tasks/edit.html', {'form':form, 'task':task})

# Deletar Tarefa:
@login_required
def taskDelete(request, id):
    task = get_object_or_404(models.Task, pk=id)
    task.delete()
    messages.info(request, "Tarefa Deletada com Sucesso")
    return redirect('/')

@login_required
def taskChange(request, id):
    task = get_object_or_404(models.Task, pk=id)

    if(task.done == 'doing'):
        task.done = 'done'
    else:
        task.done = 'doing'
    
    task.save()
    
    return redirect('/')

