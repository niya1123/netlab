from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm

def test(request):
    return HttpResponse("Hello, world. You're at the test index.")

def signup(request):
    """
    登録ビュー.
    """
    ctx={'title': 'ユーザ登録画面'}
    return render(request, 'accounts/signup.html', ctx)

class Profile(generic.TemplateView):
    template_name = 'accounts/profile.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'sns_app/index.html'