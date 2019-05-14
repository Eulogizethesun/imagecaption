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
    context={}
    file = request.FILES.get('file')  # 获取文件对象，包括文件名文件大小和文件内容
    print(file)
    response_data = {}
    response_data['fn'] = "test"
    response_data['fu'] ="test2"
    response_json_data = json.dumps(response_data)
    return HttpResponse(response_json_data)

def getcaption(request):
    response_data = {}
    response_data['fn'] = "test"
    response_data['fu'] = "test2"
    response_json_data = json.dumps(response_data)
    return HttpResponse(response_json_data)