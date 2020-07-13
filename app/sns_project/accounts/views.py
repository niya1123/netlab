from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello, world. You're at the test index.")

def signup(request):
    """
    登録ビュー.
    """
    ctx={'title': 'ユーザ登録画面'}
    return render(request, 'accounts/signup.html', ctx)