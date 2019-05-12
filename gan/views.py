from django.shortcuts import render,redirect,reverse
from .models import *
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from hashlib import sha1
import json
# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)
