# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_qiita_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DepthLearningArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('article_body', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='ImageRecognitionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('article_body', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='MachineLearningArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('article_body', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='NLPArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('article_body', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='OauthArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('article_body', models.TextField(max_length=100000)),
                ('article_token', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_token', to='django_qiita_analyzer.AccessToken')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
