from django.conf.urls import url
from django.urls import path

from . import views

# from accounts.views import PostView


urlpatterns = [
	

	url(r'^$', views.HomeView.as_view(), name='home'),
	
	

]


# url path to view main dashboard page