# Generated by Django 3.0.2 on 2020-08-11 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('question_text', models.TextField(verbose_name='本文')),
                ('is_public', models.BooleanField(default=True, verbose_name='公開する')),
                ('question_description', models.TextField(max_length=130, verbose_name='問題の説明')),
                ('keywords', models.CharField(default='問題のキーワード', max_length=255, verbose_name='問題のキーワード')),
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
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(blank=True, to='contents.Tag', verbose_name='タグ'),
        ),
    ]
