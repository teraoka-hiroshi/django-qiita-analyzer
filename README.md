# Description
### This module uses Qiita_API to obtain access token from OAUTH authentication

# pip install
>$ sudo apt-get install python3-pip 


# git clone and setup.py install
>$ cd sample_project  
$ git clone git@github.com:aporo4000/django-qiita-analyzer.git  
$ cd django-qiita-analyzer  
$ pip install -r requirements.txt   
$ python setup.py install   

 Finished!  
  
 

# Pass through the module's path
(vargrant path)   
>$ ln -fs /vagrant/django-qiita-analyzer/django_qiita_analyzer /vagrant/venv/lib/python3.5/site-packages



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
export CLIENT_ID="get client_id"  
export CLIENT_SECRET="get client_secret"  
  
>$ source .bashrc  


# Add to application 
(sample_project/settings.py)
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
    
# Write to the settings.py of the sample project
(sample_project/settings.py)    
>client_id = os.environ['CLIENT_ID']  
QIITA_API_URL="https://qiita.com/api/v2/oauth/authorize?client_id=%s&scope=%s" % (client_id, "read_qiita")  
REDIRECT_TEMPLATE_HTML='sample_application/redirect.html'


# Create Class in Views.py of sample_application
sample_application/views.py    
>(views.py) # sample code     
from django.views import View  
from django.shortcuts import render  
class sample_index(View):  
&nbsp; &nbsp; def get(self, request):  
&nbsp; &nbsp; &nbsp; &nbsp; input_class = self  
&nbsp; &nbsp; &nbsp; &nbsp; content = "GET Qiita API"  
&nbsp; &nbsp; &nbsp; &nbsp; return render(request, 'sample_application/home.html', {  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  'input_class': input_class,  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  'content': content,  
        })   
class sample_redirect(View):  
&nbsp; &nbsp; """Redirect destination"""  
&nbsp; &nbsp; def get(self, request):  
&nbsp; &nbsp; &nbsp; &nbsp; return render(request, 'sample_application/redirect.html', {})  
        
    
    
# Create sample application template
sample_application/templates/sample_application/home.html  
>(home.html)  # sample code  
  ・  
  ・  
{% load qiita_tags %}      
{% output_start_button input_class content %}  
  ・  
  ・  
 
sample_application/templates/sample_application/redirect.html  
>(redirect.html)  # sample code  
  ・  
  ・     
>\<a href="(qiita application home screen URL)">Return to home\</a>    
    ・  
    ・  

    
# Create urls.py of sample_project
sample_project/sample_project/urls.py   
Redirect to the 「RedirectView」 class of the module     
>(urls.py) # sample code  
from django.conf.urls import url  
from django.contrib import admin  
from sample_application.views import sample_index   
from django_qiita_analyzer.views import RedirectView  
from django.conf import settings  
urlpatterns = [  
&nbsp; &nbsp; url(r'^admin/', admin.site.urls),  
&nbsp; &nbsp; url(r'^(WEB home URL)/$', sample_index.as_view(), name='home'),  
&nbsp; &nbsp; url(r'^(WEB redirect URL)/$', RedirectView.as_view(template_name=settings.REDIRECT_TEMPLATE_HTML), name='home'),  
]  

 

# make and migrate and create user
>$ ./manage.py makemigrations  
$ ./manage.py migrate  
$ ./manage.py createsuperuser

# runserver
>$ ./manage.py runserver 0.0.0.0:8000  
(admin_URL) http://192.168.33.10:8000/admin/  
(Execution_URL) http://192.168.33.10:8000/(home url)/  


When you press the content name link on the home screen,  
 you go to Qiita's OAUTH authentication, if you allow it,  
  the access token is acquired and saved in the DB.

