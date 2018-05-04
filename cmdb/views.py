# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models  import Information
def infor(request):
    infor_list = Information.objects.all()
    return render_to_response('information.html',{'infor_list':infor_list})

