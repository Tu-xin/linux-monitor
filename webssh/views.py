# coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .forms import WebSshForm
import commands

def webssh(request):
    if request.method == 'POST':
        form = WebSshForm(request.POST)
        if form.is_valid():
            command = form.cleaned_data['command']
            if command.find('rm'):
                output = commands.getoutput(command)
                date=commands.getoutput('date') 
                return render(request, 'webssh.html', {'form': form,'output': output,'date':date})
            else:
                output="对不起，禁止删除！"
                date=commands.getoutput('date')
                return render(request, 'webssh.html', {'form': form,'output': output,'date':date})
    else:
        form = WebSshForm()
    return render(request, 'webssh.html', {'form': form})



def api(request,string,string02,string03):     #这里的string 就是URL那边传过来的参数
    if string == 'Tu':
        try:
            return  HttpResponse(string02)
        except Exception as e:
            return HttpResponse(string)
