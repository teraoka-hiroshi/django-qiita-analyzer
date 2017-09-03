# django-qiita-analyzer

### qiita(https://qiita.com/settings/applications/) 
#      After registering the application, make the following creation


# Add to (~/.bashrc) 
export DJANGO_QIITA_ANALYZER="~/django-qiita-analyzer/sample_application"

# The acquired client_id, client_secret Add to (.bashrc)
export CLIENT_ID="get client_id"
export CLIENT_SECRET="get client_secret"


## pip install
$ sudo apt-get install python3-pip
$ pip install -r requirements.txt 

## Environmental setting
$ vagrant up  
$ virtualenv venv  
$ source venv/bin/activate  
 

### Linking the project
(django-qiita-analyzer/link_setting.py)  
$ python link_setting.py


# Add to settings.py and urls.py of created application
(sample_application/settings.py)  
HOME_URL='sample_application/home.html'
REDIRECT_URL='sample_application/redirect.html'

(sample_application/urls.py)  
from django_qiita_analyzer.views import UpdatesView, RedirectView  
urlpatterns = [  
    url(r'^admin/', admin.site.urls),  
    # Create an html file and list it here template_name=' '  
    url(r'^django_qiita_analyzer/$', UpdatesView.as_view(template_name=HOME_URL), name='data_update'),  
    url(r'^django_qiita_analyzer/redirect/$', RedirectView.as_view(template_name=REDIRECT_URL), name='redirect'),

]



