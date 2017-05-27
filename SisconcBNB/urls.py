"""SisconcBNB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #-------include de urls de pagina---------------#
    url(r'^', include('SisconcBNB.apps.pagina.urls', namespace='pagina')),
    
    #url(r'^', include('SisconcBNB.apps.authentication.urls', namespace='authentication')),
    
    url(r'^usuario/', include('SisconcBNB.apps.authentication.urls', namespace='authentication')),
    

    #-------template de login------------------------#
    #url(r'^usuario/$',login,{'template_name': 'login/loginn.html' }, name='login'),  

    #-------include de urls de login-----------------------------------------#
    url(r'^', include('SisconcBNB.apps.habitantes.urls', namespace='habitante')),

    #-------include de urls de alumno---------------#
    #url(r'^', include('SisconcBNB.apps.alumnos.urls', namespace='alumno')),

    #-------include de urls de reportes---------------#
   # url(r'^', include('SisconcBNB.apps.reportes.urls', namespace='reportes')),

] 
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    


