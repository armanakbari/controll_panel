from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'users/register.html', context)
def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)
def home(request):
    return HttpResponse('salam')
def products(request):
    return HttpResponse('products')
def comtumer(request):
    return HttpResponse('comtumer')



