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
from django.conf.urls import url,include
from django.contrib import admin

# import django_qiita_analyzer.urls
"""
直接django_qiita_analyzer.viewのクラスをここで指定して
htmlを設定しておく
"""
from django_qiita_analyzer.views import UpdatesView, RedirectView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^django_qiita_analyzer/$', UpdatesView.as_view(template_name=settings.HOME_URL), name='data_update'),
    url(r'^django_qiita_analyzer/redirect/$', RedirectView.as_view(template_name=settings.REDIRECT_URL), name='redirect'),

]
