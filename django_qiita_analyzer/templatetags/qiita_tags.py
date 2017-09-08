from django import template
from django.utils.safestring import mark_safe
# from django.views.generic.base import TemplateView


from django.conf import settings  # settings.py
register = template.Library()

# class UpdatesView(TemplateView):
#     # template名
#     template_name = settings.HOME_URL
#
#     def get(self, request, **kwargs):
#         """
#         Qiita API
#         GET /api/v2/oauth/authorize (client_id,scope)アクセス『許可』へ
#         client_id: credentials.py
#         scope: credentials.py
#         """
#         input_class = self
#         content = 'Qiita API取得'
#         context = {
#             'input_class': input_class,
#             'content': content,
#         }
#         return self.render_to_response(context)

@register.assignment_tag
def output_start_button(input_class, content):
    """
    受け取ったqiita_api_urlでリンクボタン作成
    :param qiita_api_url: qiita_api_url
    :return: htmlタグ
    """
    mystr = '<a class="%s" href="%s">%s</a>' % (input_class, settings.QIITA_API_URL, content)
    mystr = mark_safe(mystr)
    # print(mystr)
    return mystr
