from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render, resolve_url
from django.template.loader import render_to_string
from django.views import generic

from .forms import LoginForm, UserCreateForm, ProfileUpdateForm

User = get_user_model()

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

class OnlyYouMixin(UserPassesTestMixin):
    """
    ログインしているユーザ以外にアクセスすることを防止するもの.
    """
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class Profile(OnlyYouMixin, generic.DetailView):
    """
    プロファイル.
    """
    model = User
    template_name = 'accounts/profile.html'


class ProfileUpdate(OnlyYouMixin, generic.UpdateView):
    """
    プロファイル更新
    """
    model = User
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_update.html'

    def get_success_url(self):
        return resolve_url('accounts:profile', pk=self.kwargs['pk'])