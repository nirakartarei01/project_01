from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import *
from app.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm(request)
    return render(request, 'login.html', {'form': form})
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_forms.html', {'form': form})

