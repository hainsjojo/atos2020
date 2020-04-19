from django.conf.urls import url
from django.urls import path

from . import views



urlpatterns = [
	

	url(r'^$', views.Search.as_view(), name='search'),

	


]

# url path to view search page