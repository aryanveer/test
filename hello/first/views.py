from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response,render
import requests
import json


def home(request,id=None):
    # print("test")
    response = requests.get('http://0.0.0.0:8000/api/?val=dashboard').json()
    # print("test")
    return JsonResponse(response)