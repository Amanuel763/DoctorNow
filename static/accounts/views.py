from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('home')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'this is an error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')