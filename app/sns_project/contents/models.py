# from django.db import models
# from django.utils import timezone

# class Tag(models.Model):
#     """
#     タグモデル
#     """
#     name = models.CharField('タグ名', max_length=255, unique=True)

#     def __str__(self):
#         return self.name

# class Contents(models.Model):
#     """コンテンツモデル"""
#     title = models.CharField('タイトル', max_length=32)
#     text = models.TextField('本文')
#     tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)

#     relation_posts = models.ManyToManyField('self', verbose_name='関連記事', blank=True)
#     is_public = models.BooleanField('公開可能か?', default=True)
#     description = models.TextField('記事の説明', max_length=130)
#     keywords = models.CharField('記事のキーワード', max_length=255, default='記事のキーワード')
#     created_at = models.DateTimeField('作成日', default=timezone.now)
#     updated_at = models.DateTimeField('更新日', default=timezone.now)

#     def __str__(self):
#         return self.title
