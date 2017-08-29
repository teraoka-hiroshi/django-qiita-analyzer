from django.contrib import admin

# Register your models here.

# from .models import Article, AllArticle, AccessToken
from .models import Article, AccessToken


admin.site.register(Article)
# admin.site.register(AllArticle)
admin.site.register(AccessToken)