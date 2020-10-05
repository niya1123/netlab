from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.db.models import Q
from django.http import Http404
from django.shortcuts import (get_list_or_404, get_object_or_404, render,
                              resolve_url)
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import (ContentSearchForm, CreateContentForm, CreateQuestionForm,
                    MyContentUpdateForm)
from .models import Content, Question, Tag


class CreateContent(PermissionRequiredMixin, LoginRequiredMixin, generic.edit.CreateView):
    """コンテンツ作成ビュー"""
    form_class = CreateContentForm
    template_name = 'contents/create_content.html'
    success_url = reverse_lazy('contents:create_content_done')
    permission_required = ('contents.add_content') # アプリ名.(add | delete | change )_モデル名
    raise_exception = False

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

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = ContentSearchForm(self.request.GET or None)
        if form.is_valid():
            # 選択したタグが含まれた記事
            tag = form.cleaned_data.get('tag')
            if tag:
                for t in tag:
                    queryset = queryset.filter(tag=t)

            # タイトルか本文にキーワードが含まれたもの
            # キーワードが半角スペースで区切られていれば、その回数だけfilterする。つまりAND。
            key_word = form.cleaned_data.get('key_word')
            if key_word:
                for word in key_word.split():
                    queryset = queryset.filter(Q(title__icontains=word) | Q(content_text__icontains=word))

        queryset = queryset.order_by('-updated_at').prefetch_related('tag')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ContentSearchForm(self.request.GET or None)
        return context

class MyContentList(LoginRequiredMixin, generic.ListView):
    """自分のコンテンツのリスト"""
    model = Content
    template_name = 'contents/my_content_list.html'

class MyContentUpdate(LoginRequiredMixin, generic.UpdateView):
    """自分のコンテンツの修正"""
    model = Content
    form_class = MyContentUpdateForm
    template_name = 'contents/my_content_update.html'

    def get_success_url(self):
        return resolve_url('contents:my_content_list', pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_pk'] = self.kwargs.get('pk')
        return context

class MyContentDelete(generic.DeleteView):
    """自分のコンテンツの削除"""
    model = Content
    form_class = CreateContentForm
    template_name = 'contents/my_content_delete.html'
    success_url = reverse_lazy('contents:my_content_delete_done')

class MyContentDeleteDone(generic.TemplateView):
    """削除完了画面"""
    template_name = 'contents/my_content_delete_done.html'

class MyQuestionList(LoginRequiredMixin, generic.ListView):
    """自分の問題リスト"""
    model = Question
    template_name = 'contents/my_question_list.html'

class MyQuestionUpdate(LoginRequiredMixin, generic.UpdateView):
    """自分のコンテンツの修正"""
    model = Question
    form_class = CreateQuestionForm
    template_name = 'contents/my_question_update.html'

    def get_success_url(self):
        return resolve_url('contents:my_question_list', pk=self.request.user.pk)

class ContentDetail(generic.DetailView):
    """コンテンツの詳細画面"""
    model = Content

    def get_object(self, querset=None):
        content = super().get_object()
        if content.is_public or self.request.user.is_authenticated:
            return content
        else:
            raise Http404

class QuestionList(generic.ListView):
    """問題のリスト"""
    model = Question
    template_name = 'contents/question_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_pk'] = self.kwargs.get('pk')
        return context

class QuestionDetail(generic.DetailView):
    """問題の詳細"""
    model = Question
    template_name = 'contents/question_detail.html'


class CreateTag(LoginRequiredMixin, generic.CreateView):
    """タグ作成"""
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('contents:content_list')

class CreateQuestion(LoginRequiredMixin, generic.CreateView):
    """選択肢の作成"""
    form_class = CreateQuestionForm
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
