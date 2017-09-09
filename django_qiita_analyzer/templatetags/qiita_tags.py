from django import template
from django.utils.safestring import mark_safe
from django.conf import settings  # settings.py
register = template.Library()


@register.assignment_tag
def output_start_button(input_class, content):
    """
    sample_application/views.pyから受け取る引数をHTMLタグにして返す
    input_class: クラス名
    content: リンク名
    :return: htmlタグ
    """
    mystr = '<a class="%s" href="%s">%s</a>' % (input_class, settings.QIITA_API_URL, content)
    mystr = mark_safe(mystr)
    return mystr
