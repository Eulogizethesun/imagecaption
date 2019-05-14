import os
from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
import json
# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)

def upload(request):
    obj = request.FILES.get('file')
    print(obj.name)
    f = open(os.path.join("media", obj.name), 'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()

    response_data = {}
    response_data['fn'] = "test"
    response_data['fu'] ="test2"
    response_json_data = json.dumps(response_data)
    return HttpResponse(response_json_data)

def getcaption(request):
    response_data = {}
    response_data['Hello'] = "hello"
    response_data['World'] = "world"
    response_json_data = json.dumps(response_data)
    return HttpResponse(response_json_data)

def origin(request):
    context = {}
    return render(request, 'origin.html', context)