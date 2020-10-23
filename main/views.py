from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from main.models import AppUsers
from main.serializers import AppUsersSerializer

# Create your views here.


@csrf_exempt
def mainApi(request, id=0):
    if request.method == "GET":
        res = AppUsers.objects.all()
        res_serializer = AppUsersSerializer(res, many=True)
        return JsonResponse(res_serializer.data, safe=False)
