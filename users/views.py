from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *

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

def tamrin(request):
    tamrins = Tamrin.objects.all()
    return render(request, 'users/tamrin_ostad.html', {'tamrins':tamrins})


def detailTamrin(request, tamrin_id):
    #tamrin = Responder.objects.get(id=tamrin_id)
    tamrin = Answers.objects.filter(tamrin__id=tamrin_id)
    #tamrin = Responder.objects.filter(id=tamrin.id).order_by('id')
    return render(request, 'users/tamrin_detail_ostad.html', {'tamrin': tamrin})


def comtumer(request):
    return HttpResponse('comtumer')



