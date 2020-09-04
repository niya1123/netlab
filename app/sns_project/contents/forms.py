from django import forms
from .models import Content

class CreateContentForm(forms.ModelForm):
    """コンテンツ作成フォーム"""

    class Meta:
        model = Content
        fields = ('title', 'tag', 'is_public')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'