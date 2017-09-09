from django.contrib import admin

# Register your models here.
from .models import Tag, Article, AccessToken

# from .models import OauthArticle, MachineLearningArticle, \
#     NLPArticle, ImageRecognitionArticle, DepthLearningArticle, AccessToken
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(AccessToken)

# admin.site.register(MachineLearningArticle)
# admin.site.register(NLPArticle)
# admin.site.register(ImageRecognitionArticle)
# admin.site.register(DepthLearningArticle)
