from django.conf.urls import url
from django_qiita_analyzer.views import UpdatesView, RedirectView


urlpatterns = [
    url(r'^updates/$', UpdatesView.as_view(), name='updates'),
    url(r'^redirect/$', RedirectView.as_view(), name='redirect'),
]