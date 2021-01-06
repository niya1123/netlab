from django import forms

from .models import Content, Question, Tag, Container, Port
from .widgets import CustomCheckboxSelectMultiple


class CreateContentForm(forms.ModelForm):
    """コンテンツ作成フォーム"""

    class Meta:
        model = Content
        fields = ('title', 'tag', 'content_text', 'is_public')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CreateQuestionForm(forms.ModelForm):
    """クイズ作成フォーム"""

    class Meta:
        model = Question
        fields = ('question_title', 'question_text', 'choice1', 'choice2', 'choice3', 'choice4',
              'answer')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ContentSearchForm(forms.Form):
    """コンテンツ検索フォーム"""
    key_word = forms.CharField(
        label='検索ワード',
        required=False,
    )

    tag = forms.ModelMultipleChoiceField(
        label='タグでの絞り込み',
        required=False,
        queryset=Tag.objects.order_by('name'),
        widget=CustomCheckboxSelectMultiple,
    )

class MyContentUpdateForm(forms.ModelForm):
    """自分のコンテンツ変更のフォーム"""
    class Meta:
        model = Content
        fields = ('title', 'tag', 'content_text', 'is_public')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ContainerForm(forms.ModelForm):
    """コンテナフォーム"""
    class Meta:
        model = Container
        fields = ('url', 'port_num', 'exe')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'