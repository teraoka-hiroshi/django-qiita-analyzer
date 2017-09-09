from django.db import models
from django.utils import timezone

class TokenManager(models.Manager):
    """最新のAccessTokenを取得"""
    def get_latest_token(self):
        return self.order_by('created_time').first()

class AccessToken(models.Model):
    """
    Qiita_AccessTokenを格納
    """
    token      = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now=True)  # 登録日時

    objects = models.Manager()
    latest_token = TokenManager()

    def __str__(self):
        return self.token


class ArticleManager(models.Manager):
    """最新の記事取得"""
    def check_overlap(self):
        return self.order_by('created_time').first()


class Tag(models.Model):
    """各種文献、OAuthのタグ"""
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    """記事の詳細"""
    article_title = models.CharField(max_length=50, default=None, blank=True, null=True)
    url           = models.URLField(default=None, blank=True, null=True)
    created_at    = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at    = models.DateTimeField(auto_now=False, auto_now_add=False)
    article_body  = models.TextField(max_length=100000)
    tag           = models.ManyToManyField(Tag, blank=True)
    article_token = models.ForeignKey(AccessToken, default=None, blank=True, null=True, related_name='article_token')

    def __str__(self):
        return self.article_title



