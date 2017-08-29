from setuptools import setup


setup(
    name='django-qiita-analyzer',
    version='1.0.0',
    author="Hiroshi Teraoka",
    description=("A module for users to retrieve stories from qiita using oauth"),
    license = "MIT",
    url='https://github.com/aporo4000/django-qiita-analyzer/tree/master',
    packages=['django-qiita-analyzer'],
    package_data={
        'nbupload': ['templates/django_qiita_analyzer/*.html'],
    },
)
