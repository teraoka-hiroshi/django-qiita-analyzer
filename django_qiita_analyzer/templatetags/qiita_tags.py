from django import template
from django.utils.safestring import mark_safe
from django.conf import settings  # settings.py
from modulefinder import ModuleFinder  # モジュールがあるかチェック
import subprocess  # shellコマンド実行可能

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

@register.assignment_tag
def oauth_article_acquisition_button(content_button):
    """
    OAUTHを使った記事取得ボタン(AccessToken利用)
    content_button: ボタン名
    """
    try:
        finder = ModuleFinder()  # モジュールがimportされているか確認
        finder.run_script('article_collection.py')
    except ImportError:
        print("article_collection.pyがimportされていません。")
    except FileNotFoundError:
        print("ファイル名が正しくありません")

    mystr_button = '<button type=button onclick="%s">%s</button>' % ("obtain_oauth_article()", content_button)
    mystr_button = mark_safe(mystr_button)
    return mystr_button

def obtain_oauth_article():
    """
    article_collection.pyを実行する
    """
    try:
        subprocess.check_call('python3 article_collection.py')
    except:
        print("Error.")
