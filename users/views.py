from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm, TamrinCretae, VideoCretae, CreateAnswer, ScoreOstad
from .decorator import unauthenticated_user, allowed_users, admin_only
from .models import *

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)

            messages.success(request, 'account was created for'+ username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_ostad')
        else:
            messages.info(request, 'username or password was wrong')
    context = {}
    return render(request, 'users/login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
def menuOstad(request):
    return render(request, 'users/menu_ostad.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def ostadTamrin(request):
    tamrins = Tamrin.objects.all()
    return render(request, 'users/tamrin_ostad.html', {'tamrins':tamrins})
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def ostadDetailTamrin(request, tamrin_id):
    tamrin = Answers.objects.filter(tamrin__id=tamrin_id)
    try:
        resp = Responder.objects.get(answers__id=tamrin_id)
    except Responder.DoesNotExist:
        error = "This exercise has not been answered yet!"
        return render(request, 'users/error.html', {'error':error})
    return render(request, 'users/tamrin_detail_ostad.html', {'tamrin': tamrin})
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def ostadCreateTamrin(request):
    form = TamrinCretae()
    if request.method == 'POST':
        form = TamrinCretae(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../menu_ostad/tamrin/')
    context = {'form': form}
    return render(request, 'users/ostad_create_tamrin.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def ostadUpdateTamrin(request, pk):
    tamrin_name = Tamrin.objects.get(id=pk)
    form = TamrinCretae(instance=tamrin_name)
    if request.method == 'POST':
        form = TamrinCretae(request.POST, instance=tamrin_name)
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {'form':form}
    return render(request, 'users/ostad_create_tamrin.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def videoOstadDetail(request, video_id):
    vid = Vids.objects.get(id=video_id)
    return render(request, 'users/video_detail_ostad.html', {'video':vid})
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def videoOstad(request):
    video = Vids.objects.all()
    return render(request, 'users/video_ostad.html', {'videos': video})
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def createVideo(request):
    form = VideoCretae()
    if request.method == 'POST':
        form = VideoCretae(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../videos/')
    context = {'form':form}
    return render(request, 'users/create_video.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['ostad'])
def tamrinCorrection(request, answer_id):
    answer = Answers.objects.get(id=answer_id)
    form = ScoreOstad(instance=answer)
    if request.method == 'POST':
        form = ScoreOstad(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('../tamrin/')
    context = {'form': form}
    return render(request, 'users/tamrin_ostad_tamrin_correction.html' ,context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def menuStudent(request):
    return render(request, 'users/menu_student.html')
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def studentTamrin(request):
    tamrinn = Tamrin.objects.all()
    answer = Answers.objects.all()
    tamrinn = zip(tamrinn,answer)
    return render(request, 'users/tamrin_student.html', {'tamrin':tamrinn, 'answer':answer})
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def uploadAnswer(request):
    form = CreateAnswer()
    if request.method == 'POST':
        form = CreateAnswer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {'form': form}
    return render(request, 'users/upload_answer.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def videoStudent(request):
    video = Vids.objects.all()
    context = {'video':video}
    return render(request, 'users/video_student.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def videoDetailStudent(request, video_id):
    video = Vids.objects.get(id=video_id)
    return render(request, 'users/video_detail_student.html', {'video':video})

def home(request):
    return render(request, 'users/index.html')


