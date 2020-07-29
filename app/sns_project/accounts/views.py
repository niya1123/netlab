from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
from .forms import (
    LoginForm, UserCreateForm
)

User = get_user_model()

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
    """
    ログインページ
    """
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    """
    ログアウトページ
    """
    template_name = 'sns_app/index.html'

class UserCreate(generic.CreateView):
    """
    ユーザ仮登録
    """
    template_name = 'accounts/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """
        仮登録と本登録用メールの発行.
        """
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'procotol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('mail/create/subject.txt', context)
        message = render_to_string('mail/create/message.txt', context)

        user.email_user(subject, message)
        return redirect('accounts:user_create_done')

class UserCreateDone(generic.TemplateView):
    """
    ユーザー仮登録完了
    """
    template_name = 'accounts/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    """
    メール内URLアクセス後のユーザー本登録
    """
    template_name = 'accounts/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """
        tokenをとってきて,  合っていれば本登録.
        """
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()