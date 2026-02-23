#decorators
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
#general libs
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'dashboard.html')