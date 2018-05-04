# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' =='fuweichao' and 'qq'==123456 :
        message = '欢迎你: ' + request.GET['q'].encode('utf-8')
        #message = '你的用户名是:'  + request.GET['q'].encode('utf-8'）
    else:
        message = '对不起，你不是用户fuweichao' 
    return HttpResponse(message)
