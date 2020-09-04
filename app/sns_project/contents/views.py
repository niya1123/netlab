from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import CreateContentForm
from .models import Content, Question, Tag


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

class CreateQuestion(generic.CreateView):
    """選択肢の作成"""
    model = Question
    fields = ('question_text', 'choice1', 'choice2', 'choice3', 'choice4',
              'answer')
    template_name = 'contents/create_question.html'

    def form_valid(self, form):
        content = get_object_or_404(Content, pk=self.kwargs.get('pk'))
        form.instance.content = content
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('contents:content_detail', kwargs={'pk': self.kwargs.get('pk')})

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

class AddQuestion(CreateQuestion):
    """選択肢を新規に登録する"""
    
    def form_valid(self, form):
        question = form.save()
        context = {
            'object_name': str(question),
            'object_pk': question.pk,
            'function_name': 'add_question'
        }
        return render(self.request, 'contents/close.html', context)
