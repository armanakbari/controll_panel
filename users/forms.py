from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Tamrin, Answers, Vids, Responder
from django.core.exceptions import ValidationError


class TamrinCretae(ModelForm):
    class Meta:
        model = Tamrin
        fields = '__all__'


class ScoreOstad(ModelForm):
    class Meta:
        model = Answers
        fields = ['score',]

class VideoCretae(ModelForm):
    class Meta:
        model = Vids
        fields = ['caption', 'video']

class CreateAnswer(ModelForm):
    responder = Responder.user
    class Meta:
        model = Answers
        fields = ['responder', 'tamrin', 'document',]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']