import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Tag(models.Model):
    """
    タグモデル
    """
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    """コンテンツモデル"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('タイトル', max_length=50)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', help_text='必ず1つはタグを選択してください.')
    content_text = MarkdownxField('説明文', help_text='MarkDown形式で記入可能です. ')
    is_public = models.BooleanField('公開する', default=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.content_text)

class Question(models.Model):
    """問題モデル"""
    question_title = models.CharField('問題のタイトル', max_length=50)
    question_text = models.TextField('問題文')
    choice1 = models.CharField('選択肢1', max_length=60, default='')
    choice2 = models.CharField('選択肢2', max_length=60, default='')
    choice3 = models.CharField('選択肢3', max_length=60, default='')
    choice4 = models.CharField('選択肢4', max_length=60, default='')
    CHOICES = (
        ('1', '選択肢1'),
        ('2', '選択肢2'),
        ('3', '選択肢3'),
        ('4', '選択肢4'),
    )
    answer = models.CharField('答え', max_length=60, choices=CHOICES, blank=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    """回答モデル"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')
    response = models.CharField('回答', max_length=60, blank=False)

class Review(models.Model):
    """評価"""
    SCORE_CHOICES = (
        (1, '★1'),
        (2, '★2'),
        (3, '★3'),
        (4, '★4'),
        (5, '★5'),
    )
    point = models.IntegerField('評価点', choices=SCORE_CHOICES)
    target = models.ForeignKey(Content, verbose_name='評価対象の本', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.target.title, self.get_point_display())