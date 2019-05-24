import os
from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
import json
import pickle
from gan.image_captioning import image_captioning, Vocabulary

last_pic='null'

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)

def upload(request):
    obj = request.FILES.get('file')
    print(obj.name)
    global last_pic
    last_pic=obj.name
    f = open(os.path.join("media", obj.name), 'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    print("upload success")
    response_data = {}
    response_data['fn'] = "test"
    response_data['fu'] ="test2"
    response_json_data = json.dumps(response_data)
    return HttpResponse(response_json_data)

def getcaption(request):
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global last_pic
    f='media/'+last_pic
    print(f)
    cap = image_captioning(f)
    print(cap)
    response_data = {}
    i=0
    for c in cap:
        if i==0:
            response_data['one'] = c.strip('<sos>').strip('<eos>')
            i=i+1
        elif i==1:
            response_data['two'] = c.strip('<sos>').strip('<eos>')
            i=i+1
        elif i==2:
            response_data['three'] = c.strip('<sos>').strip('<eos>')
            i=i+1
        elif i==4:
            break
    '''response_data = {}
    response_data['one'] = "test"
    response_data['two'] = "test2"
    response_data['three'] = "test3"'''
    print(response_data)
    response_json_data = json.dumps(response_data)
    print(response_json_data)
    return HttpResponse(response_json_data)

def origin(request):
    context = {}
    return render(request, 'origin.html', context)
