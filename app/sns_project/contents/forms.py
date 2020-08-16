from django import forms
from django.contrib.auth import get_user_model
from .models import Content

User = get_user_model()

class CreateContentFrom(forms.ModelForm):
    """コンテンツ作成フォーム"""

    class Meta:
        model = Content
        fields = ('title', 'tags', 'question_text', 
                  'is_public', 'question_description', 
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'