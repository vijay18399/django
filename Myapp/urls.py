from django.urls import path
from . import views


urlpatterns = [

	path("App/",views.home,{'a':[1,2,3]},name="myapp"),
	path("get/",views.get,name='get'),


]