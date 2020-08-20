from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CreateContentForm
from .models import Choice, Content, Tag


class CreateContent(LoginRequiredMixin, generic.edit.CreateView):
    """コンテンツ作成ビュー"""
    form_class = CreateContentForm
    template_name = 'contents/create_content.html'
    success_url = reverse_lazy('contents:create_content_done')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateContentDone(generic.TemplateView):
    """コンテンツ投稿完了を知らせる"""
    template_name = 'contents/create_content_done.html'

class ContentList(generic.ListView):
    """コンテンツのリスト"""
    model = Content
    template_name = 'contents/content_list.html'

class ContentDetail(generic.DetailView):
    """コンテンツの詳細画面"""
    model = Content

    def get_object(self, querset=None):
        content = super().get_object()
        if content.is_public or self.request.user.is_authenticated:
            return content
        else:
            raise Http404

class CreateTag(generic.CreateView):
    """タグ作成"""
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('contents:content_list')

class CreateChoice(generic.CreateView):
    """選択肢の作成"""
    model = Choice
    fields = '__all__'
    success_url = reverse_lazy('contents:content_list')

class AddTag(CreateTag):
    """タグを新規に登録する"""

    def form_valid(self, form):
        tag = form.save()
        context = {
            'object_name': str(tag),
            'object_pk': tag.pk,
            'function_name': 'add_tag'
        }
        return render(self.request, 'contents/close.html', context)

class AddChoice(CreateChoice):
    """選択肢を新規に登録する"""
    
    def form_valid(self, form):
        choice = form.save()
        context = {
            'object_name': str(choice),
            'object_pk': choice.pk,
            'function_name': 'add_choice'
        }
        return render(self.request, 'contents/close.html', context)