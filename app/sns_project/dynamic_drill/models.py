from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class ROOT(models.Model):
    """
    ROOTモデル．学習目標．
    """
    root_name = models.CharField('学習目標', max_length=255, unique=True)

    def __str__(self):
        return self.root_name

class EL(models.Model):
    """
    ELモデル．学習項目．
    """
    el_name = models.CharField('学習項目', max_length=255, unique=True)
    root = models.ForeignKey(ROOT, on_delete=models.CASCADE)

    def __str__(self):
        return self.el_name

class SEL(models.Model):
    """
    SELモデル．学習小目標．
    """
    sel_name = models.CharField('学習小目標', max_length=255, unique=True)
    el = models.ForeignKey(EL, on_delete=models.CASCADE)

    def __str__(self):
        return self.sel_name

class SSEL(models.Model):
    """
    SSELモデル．細目標．
    """
    ssel_name = models.CharField('細目標', max_length=255, unique=True)
    sel = models.ForeignKey(SEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.ssel_name

class QuestionTemplate(models.Model):
    """
    問題テンプレート
    """
    question_template = models.TextField('問題テンプレート')

    def __str__(self):
        return self.question_template