from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, RegisterForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'tasks/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    return render(request, 'tasks/home.html', {'tasks': tasks, 'form': form})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
    return redirect('home')

@login_required
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'tasks/home.html', {'form': form})

@login_required
def delete_task(request, pk):
    Task.objects.get(id=pk).delete()
    return redirect('home')

@login_required
def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = not task.complete
    task.save()
    return redirect('home')