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
    # 呼び出し：AccessToken.latest_token.get_latest_token()
    latest_token = TokenManager()

    def __str__(self):
        return self.token


class Article(models.Model):
    """
    Qiitaの記事を格納するクラス
    """
    article_title        = models.CharField(max_length=50, default=None, blank=True, null=True)
    url          = models.URLField(default=None, blank=True, null=True)
    created_at   = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at   = models.DateTimeField(auto_now=False, auto_now_add=False)
    article_body = models.TextField(max_length=100000)
    article_token = models.ForeignKey(AccessToken, default=None, blank=True, null=True, related_name='article_token')

    def __str__(self):
        return self.article_title

# class AllArticle(models.Model):
#     """
#     Qiitaの記事を格納するクラス
#     """
#     article_title        = models.CharField(max_length=50, default=None, blank=True, null=True)
#     url          = models.URLField(default=None, blank=True, null=True)
#     created_at   = models.DateTimeField(auto_now=False, auto_now_add=False)
#     updated_at   = models.DateTimeField(auto_now=False, auto_now_add=False)
#     article_body = models.TextField(max_length=100000)
#     # article_token = models.ForeignKey(AccessToken, default=None, blank=True, null=True, related_name='article_token')
#
#     def __str__(self):
#         return self.article_title