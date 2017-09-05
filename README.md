# django-qiita-analyzer(AccessToken)

## pip install
>$ sudo apt-get install python3-pip  
$ pip install -r requirements.txt 

# git clone and setup.py install
>$ cd sample_project  
$ git clone git@github.com:aporo4000/django-qiita-analyzer.git  
$ cd django-qiita-analyzer  
$ python setup.py install   

 Finished!   

# Pass through the module's path
(vargrant path)   
>$ ln -fs /vagrant/django-qiita-analyzer/django_qiita_analyzer /vagrant/venv/lib/python3.5/site-packages'



# Register qiita application  
### qiita(https://qiita.com/settings/applications/) 

get client_id  
get client_secret

# Django start
### create project + application
>$ django-admin startproject (sample_project)  
>$ ./manage.py startapp (sample_application)  

# Add to PATH (~/.bashrc) 
>export DJANGO_QIITA_ANALYZER="~/(create project name)"  
export APPLICATION_NAME='(create applicaiton name)'  
export CLIENT_ID="(get client_id)"  
export CLIENT_SECRET="(get client_secret)" 
  
>$ source .bashrc  


### Add to (project_name/settings.py)
>ALLOWED_HOSTS = ["*"]  
INSTALLED_APPS = [  
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',   
    'django_qiita_analyzer', # <-- Add   
    '(create applicaiton name)', # <-- Add   
    ]


# Create sample application template
(PATH)sample_application/templates/sample_application/home.html  
(home.html)  # To write  
>{% load qiita_tags %}      
{% output_button qiita_api_url %}   
 
(PATH)sample_application/templates/sample_application/redirect.html  
(redirect.html)  # To write  
>\<p>{{ token }}\</p>  



# Write to the settings.py of the sample project
(sample_application/settings.py)    
>HOME_URL='sample_application/home.html'
REDIRECT_URL='sample_application/redirect.html'


# Write to the urls.py of the sample project
(sample_application/urls.py)  
>from django.conf.urls import url,include  
from django.contrib import admin
from django-qiita-analyzer.django_qiita_analyzer.views import UpdatesView, RedirectView 
from django.conf import settings
 
>urlpatterns = [  
    url(r'^admin/', admin.site.urls),  
    # Create an html file and list it here template_name=' '  
    url(r'^django_qiita_analyzer/$', UpdatesView.as_view(template_name=settings.HOME_URL), name='data_update'),  
    url(r'^django_qiita_analyzer/redirect/$', RedirectView.as_view(template_name=settings.REDIRECT_URL), name='redirect'),  
]
 


# Write to models.py of sample application
(sample_application/models.py)  
>from django.db import models  
from django.utils import timezone  
  
>class TokenManager(models.Manager):  
    """最新のAccessTokenを取得"""  
    def get_latest_token(self):  
        return self.order_by('created_time').first()  

>class AccessToken(models.Model):  
    """  
    Qiita_AccessTokenを格納  
    """  
    token      = models.CharField(max_length=50)  
    created_time = models.DateTimeField(auto_now=True)  # 登録日時  
   objects = models.Manager()  
    # 呼び出し：AccessToken.latest_token.get_latest_token()  
    latest_token = TokenManager()  
   def __str__(self):  
        return self.token  

>class ArticleManager(models.Manager):  
    """最新の記事取得"""  
    def check_overlap(self):  
        return self.order_by('created_time').first()  

>class OauthArticle(models.Model):  
    """  
    Oauthを使ってQiitaの記事を格納するクラス  
    """  
    article_title        = models.CharField(max_length=50, default=None, blank=True, null=True)  
    url          = models.URLField(default=None, blank=True, null=True)  
    created_at   = models.DateTimeField(auto_now=False, auto_now_add=False)  
    updated_at   = models.DateTimeField(auto_now=False, auto_now_add=False)  
    article_body = models.TextField(max_length=100000)  
    article_token = models.ForeignKey(AccessToken, default=None, blank=True, null=True, related_name='article_token')  
   def __str__(self):  
        return self.article_title  


# Write to admin.py of sample project
>from .models import  AccessToken  
admin.site.register(AccessToken)

# make and migrate and create user
>$ ./manage.py makemigrations  
$ ./manage.py migrate  
$ ./manage.py createsuperuser

# runserver
>$ ./manage.py runserver 0.0.0.0:8000  
(admin_URL) http://192.168.33.10:8000/admin/  
(Execution_URL) http://192.168.33.10:8000/django_qiita_analyzer/


