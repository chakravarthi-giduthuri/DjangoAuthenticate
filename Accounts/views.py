from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'registration done')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def home(request):
    return render(request, 'Home.html')

# def save(request):
# 	return render(request,'save.html',{})
