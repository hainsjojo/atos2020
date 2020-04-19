from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	
	 url(r'^$', views.newhome, name='newhome'),


]

# url path to view the login page