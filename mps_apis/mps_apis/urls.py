"""mps_apis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# from .views import sample_index(サンプルで作成するhomeクラス)
"""
モジュールのdjango_qiita_analyzer.viewのクラスをここで指定する
settings.pyにリダイレクトするHTML名を指定しておき呼び出す
"""
from django_qiita_analyzer.views import RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^django_qiita_analyzer/$', sample_index.as_view(), name='home'),
    url(r'^django_qiita_analyzer/redirect/$', RedirectView.as_view(template_name=settings.REDIRECT_HTML), name='redirect'),

]
