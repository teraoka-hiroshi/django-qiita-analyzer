from django.conf.urls import url
from django_qiita_analyzer.views import RedirectView


urlpatterns = [
    url(r'^redirect/$', RedirectView.as_view(), name='redirect'),
]