import os


# リンクを通すコマンド実行
"""
通常djangoプロジェクトを作成したプロジェクトフォルダの直下に
アプリケーションフォルダ(django_qiita_analyzer)を作成しないといけない為、
このモジュールではpythonのsite-packagesへシンボリックリンクを貼るようにしている
"""
os.system('ln -fs /vagrant/django-qiita-analyzer/django_qiita_analyzer /vagrant/venv/lib/python3.5/site-packages')

