# coding:utf-8
import datetime
from django.shortcuts import render,redirect,HttpResponse
from . import models
from . import forms
import commands
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    date=commands.getoutput('date')
    area=commands.getoutput('sh /home/Tu/Linux_form/monitor/ip.sh 2>/dev/null ')
    weather=commands.getoutput('python  /home/Tu/Linux_form/monitor/weather.py  ')
    username = request.session.get('user',None)
    if  username:
        return render(request,'index.html',{'date': date,'area': area,'weather':weather,'username':username})
    #if not request.user.is_authenticated:    
       # return   redirect('/login/')
    else:
        return   redirect('/login/')
        
       # obj = forms.loginForm()
        #return render(request, 'login.html', {'form': obj})

def Login(request):
    # print(request.POST)
    if request.method == 'GET':
        obj = forms.loginForm()
        # print('GET')
        return render(request, 'login.html', {'form': obj})
    if request.method == 'POST':
        # print(request.POST)
        obj = forms.loginForm(request.POST)
        if obj.is_valid():    #PSOT值合法
            data = obj.cleaned_data       #提交的所有值
            username = data.get('username')
            password = data.get('pwd')
            user = models.User.objects.filter(username=username, password=password)
            #user = authenticate(username=username, password=password)
            if user :
                request.session.set_expiry(60 * 30)            
                request.session['is_login'] = 'true'
                request.session['user']=username
                #login(request,user)
                return redirect('/index')
            else:
                return HttpResponse('chucuole')
                #errors =  "用户名或密码不正确！"
                #return render(request, 'login.html', {'errors': errors})
        else:
            errors =  "用户名或密码不正确！"
            return render(request, 'login.html', {'errors': errors,'form': obj})
            #return render(request, 'login.html', {'form': obj})
       

def logout(request):
    try:
        #删除is_login对应的value值
        del request.session['is_login']
        del request.session['user']
    except KeyError:
        pass
    #点击注销之后，直接重定向回登录页面
    return redirect('/login/')

def register(request):

    if request.method == 'GET':
        obj = forms.RegisterForm()
        return render(request,'register.html',{'form':obj})
    elif request.method == 'POST':
        obj = forms.RegisterForm(request.POST)
        if obj.is_valid():
            data = obj.cleaned_data
            #pwd1 = data.get('pwd')
            username= request.POST.get('username')
            password= request.POST.get('pwd')
            email= request.POST.get('email')
            if username:
                models.User.objects.create(username=username,password =password,email = email )
                return redirect('/login/')
                #return HttpResponse(str(pwd1))
            else:
                return HttpResponse('username字段为空')
        else:
            errors = obj.errors
            return  render(request,'register.html',{'form':obj,'errors':errors})

            
            
def deluser(request):
    obj = forms.loginForm()
    username = request.session.get('user',None)
    delusers =  models.User.objects.filter(username = username).delete()
    deltxt = str(username)+"被删除成功"
    return render(request,'login.html',{'deltxt':deltxt,'form':obj})
    




