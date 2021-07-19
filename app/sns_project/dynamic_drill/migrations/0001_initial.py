# Generated by Django 3.0.2 on 2021-07-19 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('el_name', models.CharField(max_length=255, unique=True, verbose_name='学習項目')),
            ],
        ),
        migrations.CreateModel(
            name='ROOT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_name', models.CharField(max_length=255, unique=True, verbose_name='学習目標')),
            ],
        ),
        migrations.CreateModel(
            name='SEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sel_name', models.CharField(max_length=255, unique=True, verbose_name='学習小目標')),
                ('el', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_drill.EL')),
            ],
        ),
        migrations.CreateModel(
            name='SSEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssel_name', models.CharField(max_length=255, unique=True, verbose_name='細目標')),
                ('sel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_drill.SEL')),
            ],
        ),
        migrations.AddField(
            model_name='el',
            name='root',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_drill.ROOT'),
        ),
    ]
