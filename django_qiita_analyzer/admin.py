from django.contrib import admin

# Register your models here.

from .models import OauthArticle, MachineLearningArticle, \
    NLPArticle, ImageRecognitionArticle, DepthLearningArticle, AccessToken


admin.site.register(OauthArticle)
admin.site.register(MachineLearningArticle)
admin.site.register(NLPArticle)
admin.site.register(ImageRecognitionArticle)
admin.site.register(DepthLearningArticle)
admin.site.register(AccessToken)