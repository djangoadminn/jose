from django.conf.urls import url
from django.contrib import admin
from  SisconcBNB.apps.authentication.views  import HomeTemplateView,LoginView,LogoutView
from .views import HomeTemplateView,LoginView,LogoutView


urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]