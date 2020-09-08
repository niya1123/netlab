from django import forms
from .models import Content, Tag

class CreateContentForm(forms.ModelForm):
    """コンテンツ作成フォーム"""

    class Meta:
        model = Content
        fields = ('title', 'tag', 'content_text', 'is_public')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ContentSearchForm(forms.Form):
    """コンテンツ検索フォーム"""
    keyword = forms.CharField(
        label='検索ワード',
        required=False,
    )

    tag = forms.ModelMultipleChoiceField(
        label='タグでの絞り込み',
        required=False,
        queryset=Tag.objects.order_by('name'),
    )