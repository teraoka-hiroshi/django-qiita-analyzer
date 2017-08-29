from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.assignment_tag
def output_button(qiita_api_url):
    """
    受け取ったqiita_api_urlでリンクボタン作成
    :param qiita_api_url: qiita_api_url
    :return: htmlタグ
    """
    mystr = '<a href="%s"><button type="submit">Qiita_API取得</button></a>' % qiita_api_url
    mystr = mark_safe(mystr)
    # print(mystr)
    return mystr
