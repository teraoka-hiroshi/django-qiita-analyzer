from setuptools import setup


setup(
    name='django_qiita_analyzer',
    version='1.0.0',
    author="Hiroshi Teraoka",
    description=("A module for users to retrieve stories from qiita using oauth"),
    license = "MIT",
    url='https://github.com/aporo4000/django-qiita-analyzer',
    packages=['django_qiita_analyzer'],
    package_data={
        'django_qiita_analyzer': ['migrations/*.py'],
        'django_qiita_analyzer': ['templates/django_qiita_analyzer/*.html'],
        'django_qiita_analyzer': ['templatetags/*.py'],
    },
)
