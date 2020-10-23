# restFramework-Django
Setting Django Framework with API for outside FrontEnd frameworks like Angular and React (with GET example)

This repository is an example of a Django project with settings for API. It includes one GET method.

Here is all the process to these settings from scratch:

1) activate project environment (project-name/scripts/activate.bat)
2) pip install djangorestframework
3) pip install django-cors-headers
4) add in project/settings.py: 
	INSTALLED_APPS = ['corsheaders', 'rest_framework',]
	CORS_ORIGIN_ALLOW_ALL = True (or) CORS_ORIGIN_WHITLIST = ('http://127.0.0.1')
	MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware',]
5) create models in app-name/models.py, for example:
	class AppUsers(models.Model):
	FirstName = models.CharField(max_length=100)
	LastName = models.CharField(max_length=100)
	Age = models.IntegerField()
	Married = models.BooleanField()
6) python manage.py makemigrations app-name
7) python manage.py migrate
8) create file: app-name/serializers.py
9) in serializers:
	from rest_framework import serializers
	from Main.models import AppUsers

	class AppUsersSerializer(serializers.ModelSerializer):
	    class Meta:
	        model = AppUsers
	        fields = ('FirstName', 'LastName', 'Age', 'Married',)
10) in views.py:
	from django.shortcuts import render
	from django.views.decorators.csrf import csrf_exempt
	from rest_framework.parsers import JSONParser
	from django.http.response import JsonResponse
	from main.models import AppUsers
	from main.serializers import AppUsersSerializer

	@csrf_exempt
	def mainApi(request, id=0):
	    if request.method == "GET":
	        res = AppUsers.objects.all()
	        res_serializer = AppUsersSerializer(res, many=True)
	        return JsonResponse(res_serializer.data, safe=False)
11) create urls.py in app folder and write:
	from django.urls import path
	from . import views
	from django.conf.urls import url

	urlpatterns = [
	    path("", views.index, name="index"),
	    path('mainApi/', views.mainApi)
	]
12) in project folder/urls.py add:
	from django.urls import path, include
	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include("main.urls")),
	]
  
  * To see some data, please notice that you need to add data to your sql. This repository already has some data.
  To add data of your own, notice you need to create a super user as these next stages show:
  
1)  in the command line, in the project directory: python manage.py createsuperuser
2) add in project/admin.py: 
	from .models import model-name
	admin.site.register(model-name)

  
