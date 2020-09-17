# Generated by Django 3.0.2 on 2020-09-17 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markdownx.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('content_text', markdownx.models.MarkdownxField(help_text='MarkDown形式で記入可能です. ', verbose_name='説明文')),
                ('is_public', models.BooleanField(default=True, verbose_name='公開する')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(choices=[(1, '★1'), (2, '★2'), (3, '★3'), (4, '★4'), (5, '★5')], verbose_name='評価点')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.Content', verbose_name='評価対象の本')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=50, verbose_name='問題のタイトル')),
                ('question_text', models.TextField(verbose_name='問題文')),
                ('choice1', models.CharField(default='', max_length=60, verbose_name='選択肢1')),
                ('choice2', models.CharField(default='', max_length=60, verbose_name='選択肢2')),
                ('choice3', models.CharField(default='', max_length=60, verbose_name='選択肢3')),
                ('choice4', models.CharField(default='', max_length=60, verbose_name='選択肢4')),
                ('answer', models.CharField(blank=True, choices=[('1', '選択肢1'), ('2', '選択肢2'), ('3', '選択肢3'), ('4', '選択肢4')], max_length=60, verbose_name='答え')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.Content')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='tag',
            field=models.ManyToManyField(blank=True, to='contents.Tag', verbose_name='タグ'),
        ),
    ]
