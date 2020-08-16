from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Tag(models.Model):
    """
    タグモデル
    """
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name

class Content(models.Model):
    """コンテンツモデル"""
    title = models.CharField('タイトル', max_length=50)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    question_text = models.TextField('本文')

    is_public = models.BooleanField('公開する', default=True)
    question_description = models.TextField('問題の説明', max_length=130)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return self.title

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