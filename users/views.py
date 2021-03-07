from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import CreateUserForm, TamrinCretae, VideoCretae, CreateAnswer, ScoreOstad
from django.views import View
from django.utils.decorators import method_decorator
from .decorator import unauthenticated_user, allowed_users, admin_only
from .models import *



class RegisterPage(View):
    @method_decorator(unauthenticated_user)
    def get(self, request):
        form = CreateUserForm()
        context = {'form':form}
        return render(request, 'users/register.html', context)

    @method_decorator(unauthenticated_user)
    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='student')
            user.groups.add(group)
            Responder.objects.create(user=user)
            messages.success(request, 'account was created for' + username)
            return redirect('login')
        context = {'form': form}
        return render(request, 'users/register.html', context)
class LoginPage(View):
    @method_decorator(unauthenticated_user)
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, 'users/login.html', context)

    @method_decorator(unauthenticated_user)
    def post(self,request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, password=password, email=email)
        if user is not None:
            login(request, user)
            gr = request.user.groups.all()[0].name
            if gr == 'student':
                return redirect('menu_student')
            elif gr == 'ostad':
                return redirect('menu_ostad')
        else:
            messages.info(request, 'username or password was wrong')
            context = {}
            return render(request, 'users/login.html', context)
class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class MenuOstad(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(admin_only)
    def get(self,request):
        return render(request, 'users/menu_ostad.html')
    def post(self,request):
        return render(request, 'users/menu_ostad.html')
class OstadTamrin(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request):
        tamrins = Tamrin.objects.all()
        return render(request, 'users/tamrin_ostad.html', {'tamrins':tamrins})
class OstadDetailTamrin(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request, tamrin_id):
        #tamrin = Answers.objects.filter(tamrin__id=tamrin_id)

        resp = Responder.objects.all()

        tmp = []
        for i in resp:
            try:
                g = Answers.objects.get(responder__id=i.id, tamrin__id=tamrin_id)
                tmp.append([i, g])
            except:
                g = 0
                tmp.append([i, g])

        return render(request, 'users/tamrin_detail_ostad.html', {'tamrin':tmp})
class OstadCreateTamrin(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request):
        form = TamrinCretae()
        context = {'form': form}
        return render(request, 'users/ostad_create_tamrin.html', context)
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def post(self, request):
        form = TamrinCretae(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../menu_ostad/tamrin/')
        context = {'form': form}
        return render(request, 'users/ostad_create_tamrin.html', context)
class OstadUpdateTamrin(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request, pk):
        tamrin_name = Tamrin.objects.get(id=pk)
        form = TamrinCretae(instance=tamrin_name)
        context = {'form':form}
        return render(request, 'users/ostad_create_tamrin.html', context)

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def post(self, request, pk):
        tamrin_name = Tamrin.objects.get(id=pk)
        form = TamrinCretae(request.POST, instance=tamrin_name)
        if form.is_valid():
            form.save()
            return redirect('../')
        context = {'form': form}
        return render(request, 'users/ostad_create_tamrin.html', context)
class VideoOstadDetail(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request, video_id):
        vid = Vids.objects.get(id=video_id)
        return render(request, 'users/video_detail_ostad.html', {'video':vid})
class VideoOstad(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request):
        video = Vids.objects.all()
        return render(request, 'users/video_ostad.html', {'videos': video})
class CreateVideo(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request):
        form = VideoCretae()
        context = {'form':form}
        return render(request, 'users/create_video.html', context)

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def post(self, request):
        form = VideoCretae(request.POST, request.FILES)
        name = request.FILES['video'].name
        if form.is_valid():
            if ".mp4" in name:
                form.save()
                return redirect('../videos/')
            else:
                messages.info(request, 'you should upload a mp4 file')
        context = {'form': form}
        return render(request, 'users/create_video.html', context)
class TamrinCorrection(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def get(self, request, answer_id):
        answer = Answers.objects.get(id=answer_id)
        form = ScoreOstad(instance=answer)
        context = {'form': form}
        return render(request, 'users/tamrin_ostad_tamrin_correction.html' ,context)

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['ostad']))
    def post(self, request, answer_id):
        answer = Answers.objects.get(id=answer_id)
        form = ScoreOstad(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('../')
        context = {'form': form}
        return render(request, 'users/tamrin_ostad_tamrin_correction.html', context)

class MenuStudent(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['student']))
    def get(self, request):
        return render(request, 'users/menu_student.html')
class StudentTamrin(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['student']))
    def get(self, request):
        tamrinn = Tamrin.objects.all()
        answer = Answers.objects.all()
        tmp = []
        for i in tamrinn:
            try:
                r = request.user.responder.id
                g = Answers.objects.get(tamrin__id=i.id, responder__id=r)
                tmp.append([i,g])
            except:
                g = 0
                tmp.append([i, g])

        return render(request, 'users/tamrin_student.html', {'answer':tmp})
class UploadAnswer(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['student']))
    def get(self, request, tamrin_id):
        try:
            answer = Answers.objects.get(id=tamrin_id)
            form = CreateAnswer(instance=answer)
        except:
            form = CreateAnswer()
        tam = Tamrin.objects.get(id=tamrin_id)
        context = {'form': form, 'tamrin':tam}
        return render(request, 'users/upload_answer.html', context)

    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['student']))
    def post(self, request, tamrin_id):
        try:
            answer = Answers.objects.get(id=tamrin_id)
            form = CreateAnswer(request.POST, request.FILES, instance=answer)
            if form.is_valid():
                form.save()
                return redirect('../')
        except:
            form = CreateAnswer(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('../')
        tam = Tamrin.objects.get(id=tamrin_id)
        context = {'form': form, 'tamrin': tam}
        return render(request, 'users/upload_answer.html', context)
class VideoStudent(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['student']))
    def get(self, request):
        video = Vids.objects.all()
        context = {'video':video}
        return render(request, 'users/video_student.html', context)
class VideoDetailStudent(View):
    @method_decorator(login_required(login_url='login'))
    @method_decorator(allowed_users(allowed_roles=['student']))
    def get(self, request, video_id):
        video = Vids.objects.get(id=video_id)
        return render(request, 'users/video_detail_student.html', {'video':video})

class Home(View):
    def get(self, request):
        return render(request, 'users/index.html')

def handler(request, exception):
    return render(request, 'users/404.html')

