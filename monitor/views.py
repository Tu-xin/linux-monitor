# coding:utf-8
from django.shortcuts import render,render_to_response,redirect
import os
import sys
import commands
import time
import json
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django import forms
from django.template import RequestContext
from django.contrib import auth
from cmdb.models  import Information
from django.http import HttpResponse
from Linux_form.settings import TIME_JS_REFRESH, TIME_JS_REFRESH_LONG, TIME_JS_REFRESH_NET
from webssh.forms import WebSshForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required 
import platform
import multiprocessing
from datetime import timedelta

time_refresh = TIME_JS_REFRESH
time_refresh_long = TIME_JS_REFRESH_LONG
time_refresh_net = TIME_JS_REFRESH_NET




def servers(request):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if request.method == 'POST':
        hostgroup = request.POST.get("hostgroup","")    
        model = request.POST.get("model","")    
        user = request.POST.get("user","")    
        command = request.POST.get("command","") 
        os.environ['hostgroup']=str(hostgroup)
        os.environ['model']=str(model)
        os.environ['user']=str(user)
        os.environ['command']=str(command)
        output = commands.getoutput("sh /home/Tu/Linux_form/monitor/ansible.sh $hostgroup $model $user $command")
        return render(request,'servers.html',{'output':output})
    return render(request,'servers.html')



def filersync(request):
    reload(sys)
    sys.setdefaultencoding('utf-8')  #设置编码
    if request.method == 'POST':
        hostgroup = request.POST.get("hostgroup","")#从前端输入获取hostgroup
        srcname = request.POST.get("srcname","")
        destname = request.POST.get("destname","")
        os.environ['hostgroup']=str(hostgroup) #加入环境变量
        os.environ['srcname']=str(srcname)
        os.environ['destname']=str(destname)
        output = commands.getoutput("sh /home/Tu/Linux_form/monitor/filersync.sh $hostgroup   $srcname  $destname")
        return render(request,'filersync.html',{'output':output})
    return render(request,'filersync.html')



def program(request):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if request.method == 'POST':
        hostgroup = request.POST.get("hostgroup","")
        service = request.POST.get("service","")
        status = request.POST.get("status","")
        os.environ['hostgroup']=str(hostgroup)
        os.environ['service']=str(service)
        os.environ['status']=str(status)
        output = commands.getoutput("sh /home/Tu/Linux_form/monitor/program.sh $hostgroup $service $status ")
        return render(request,'program.html',{'output':output})
    return render(request,'program.html')



def monitorset(request):
    if request.method == 'POST':
        servername =  request.POST.get("servername","")
        item =  request.POST.get("item","")
        value =  request.POST.get("value","")
        serverip  =  request.POST.get("serverip","")
        time = time.strftime("%H:%M:%S", time.localtime())
        try:
             host = monitors.objects.filter(servername=servername,item=item).get().servername
             return HttpResponse('已经有这个监控项了')
        except:
            monitors.objects.create(servername=servername,item=item,value=value,serverip=serverip,time=time)
            return HttpResponse('创建了这个监控项') 

    return render(request,'monitorset.html')

#@login_required(login_url='/login/')
def server(request):
     infor_list = Information.objects.all()
     return render_to_response('server.html',{'infor_list':infor_list})



def monitort(request):
     os.system('sh /home/Tu/Linux_form/monitor/image.sh')
     return render(request,'monitort.html')


def websshtest(request):
    if request.method == 'POST':
        form = WebSshForm(request.POST)
        if form.is_valid():
            command = form.cleaned_data['command']
            if command.find('rm'):
                output = commands.getoutput(command)
                date=commands.getoutput('date') 
                return render(request, 'websshn.html', {'form': form,'output': output,'date':date})
            else:
                 rmdata="对不起，禁止删除！"
                 return render(request, 'websshn.html', {'rmdata':rmdata})
    else:
        form = WebSshForm()
    return render(request, 'websshn.html', {'form': form})


def servicemanage(request):
    return HttpResponse('程序启动成功')


def experience(request):
    username = request.session.get('user',None)
    if username is None:    
        return   redirect('/login/')
    else :
        date=commands.getoutput('date')
        infor_list = Experience.objects.all()
    return render_to_response('experience.html',{'date': date,'infor_list':infor_list})



def linuxlog(request):
    date=commands.getoutput('date')
    return render_to_response('linuxlog.html',{'date':date})

def servicelog(request):
    date=commands.getoutput('date')
    return render_to_response('servicelog.html',{'date':date})




def cpu(request):
    os.system('sh /home/Tu/Linux_form/monitor/image.sh')
    return render_to_response('cpu.html')

def memory(request):
    os.system('sh /home/Tu/Linux_form/monitor/image.sh')
    return render_to_response('memory.html')

def disk(request):
    data = os.system('sh /home/Tu/Linux_form/monitor/image.sh')
    return  response('邮件已发送')

     
def getnetstat(request):
    """
    Return netstat output
    """
    try:
        net_stat = get_netstat()
    except Exception:
        net_stat = None

    data = json.dumps(net_stat)
    response = HttpResponse()
    #response['Content-Type'] = "text/javascript"
    response.write(data)
    return response
    
def platform(request, name):
    """
    Return the hostname
    """
    data = commands.getoutput("python /home/Tu/Linux_form/monitor/get.py")
    data = eval(data)
    if name == 'hostname':
        try:
            data = data['hostname']
        except Exception:
            data = None

    if name == 'osname':
        try:
            data = data['osname']
        except Exception:
            data = None

    if name == 'kernel':
        try:
            data = data['kernel']
        except Exception:
            data = None
            
    data = json.dumps(data)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response



def getcpus(request, name):
    """
    Return the CPU number and type/model
    """
    cpus = get_cpus()
    cputype = cpus['type']
    cpucount = cpus['cpus']
    data = {}

    if name == 'type':
        try:
            data = cputype
        except Exception:
            data = None

    if name == 'count':
        try:
            data = cpucount
        except Exception:
            data = None

    data = json.dumps(data)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response


def uptime(request):
    """
    Return uptime
    """
    try:
        up_time = get_uptime()
    except Exception:
        up_time = None

    data = json.dumps(up_time)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response


def getdisk(request):
    """
    Return the disk usage
    """
    try:
        diskusage = get_disk()
    except Exception:
        diskusage = None
    data = json.dumps(diskusage)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response


def getips(request):
    """
    Return the IPs and interfaces
    """
    try:
        get_ips = get_ipaddress()
    except Exception:
        get_ips = None

    data = json.dumps(get_ips['itfip'])
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response


def getusers(request):
    """
    Return online users
    """
    try:
        online_users = get_users()
    except Exception:
        online_users = None

    data = json.dumps(online_users)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response
    
    


def getproc(request):
    """
    Return the running processes
    """
    try:
        processes = get_cpu_usage()
        processes = processes['all']
    except Exception:
        processes = None

    data = json.dumps(processes)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response


def cpuusage(request):
    """
    Return CPU Usage in %
    """
    try:
        cpu_usage = get_cpu_usage()
    except Exception:
        cpu_usage = 0
    cpu = [
        {
            "value": cpu_usage['free'],
            "color": "#0AD11B"
        },
        {
            "value": cpu_usage['used'],
            "color": "#F7464A"
        }
    ]

    data = json.dumps(cpu)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(data)
    return response



def memusage(request):
    """
    Return Memory Usage in % and numeric
    """
    datasets_free = []
    datasets_used = []
    datasets_buffers = []
    datasets_available = []

    try:
        mem_usage = get_mem()
    except Exception:
        mem_usage = 0

    try:
        cookies = request.COOKIES['memory_usage']
    except Exception:
        cookies = None

    if not cookies:
        datasets_free.append(0)
        datasets_used.append(0)
        datasets_buffers.append(0)
        datasets_available.append(0)
    else:
        datasets = json.loads(cookies)
        datasets_free = datasets[0]
        datasets_used = datasets[1]
        datasets_buffers = datasets[2]
        datasets_available = datasets[3]

    if len(datasets_free) > 10:
        while datasets_free:
            del datasets_free[0]
            if len(datasets_free) == 10:
                break
    if len(datasets_used) > 10:
        while datasets_used:
            del datasets_used[0]
            if len(datasets_used) == 10:
                break
    if len(datasets_buffers) > 10:
        while datasets_buffers:
            del datasets_buffers[0]
            if len(datasets_buffers) == 10:
                break
    if len(datasets_available) > 10:
        while datasets_available:
            del datasets_available[0]
            if len(datasets_available) == 10:
                break
    if len(datasets_free) <= 9:
        datasets_free.append(int(mem_usage['freemem']))
    if len(datasets_free) == 10:
        datasets_free.append(int(mem_usage['freemem']))
        del datasets_free[0]
    if len(datasets_used) <= 9:
        datasets_used.append(int(mem_usage['usage']))
    if len(datasets_used) == 10:
        datasets_used.append(int(mem_usage['usage']))
        del datasets_used[0]
    if len(datasets_buffers) <= 9:
        datasets_buffers.append(int(mem_usage['buffers']))
    if len(datasets_buffers) == 10:
        datasets_buffers.append(int(mem_usage['buffers']))
        del datasets_buffers[0]
    if len(datasets_available) <= 9:
        datasets_available.append(int(mem_usage['availamem']))
    if len(datasets_available) == 10:
        datasets_available.append(int(mem_usage['availamem']))
        del datasets_available[0]


    if len(datasets_free) == 10:
        if sum(datasets_free) == 0:
            datasets_free[9] += 0.1
        if sum(datasets_free) / 10 == datasets_free[0]:
            datasets_free[9] += 0.1

    memory = {
        'labels': [""] * 10,
        'datasets': [
            {
                "fillColor": "rgba(247,70,74,0.5)",
                "strokeColor": "rgba(247,70,74,1)",
                "pointColor": "rgba(247,70,74,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_used
            },
            {
                "fillColor": "rgba(43,214,66,0.5)",
                "strokeColor": "rgba(43,214,66,1)",
                "pointColor": "rgba(43,214,66,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_free
            },
            {
                "fillColor": "rgba(0,154,205,0.5)",
                "strokeColor": "rgba(0,154,205,1)",
                "pointColor": "rgba(0,154,205,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_buffers
            },
            {
                "fillColor": "rgba(255,185,15,0.5)",
                "strokeColor": "rgba(255,185,15,1)",
                "pointColor": "rgba(265,185,15,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_available
            }
        ]
    }

    cookie_memory = [datasets_free, datasets_used, datasets_buffers, datasets_available]
    data = json.dumps(memory)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.cookies['memory_usage'] = cookie_memory
    response.write(data)
    return response



def loadaverage(request):
    """
    Return Load Average numeric
    """
    datasets = []

    try:
        load_average = get_load()
    except Exception:
        load_average = 0

    try:
        cookies = request.COOKIES['load_average']
    except Exception:
        cookies = None

    if not cookies:
        datasets.append(0)
    else:
        datasets = json.loads(cookies)
    if len(datasets) > 10:
        while datasets:
            del datasets[0]
            if len(datasets) == 10:
                break
    if len(datasets) <= 9:
        datasets.append(float(load_average))
    if len(datasets) == 10:
        datasets.append(float(load_average))
        del datasets[0]

    # Some fix division by 0 Chart.js
    if len(datasets) == 10:
        if sum(datasets) == 0:
            datasets[9] += 0.1
        if sum(datasets) / 10 == datasets[0]:
            datasets[9] += 0.1

    load = {
        'labels': [""] * 10,
        'datasets': [
            {
                "fillColor": "rgba(151,187,205,0.5)",
                "strokeColor": "rgba(151,187,205,1)",
                "pointColor": "rgba(151,187,205,1)",
                "pointStrokeColor": "#fff",
                "data": datasets
            }
        ]
    }

    data = json.dumps(load)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.cookies['load_average'] = datasets
    response.write(data)
    return response



def gettraffic(request):
    """
    Return the traffic for the interface
    """
    datasets_in = []
    datasets_in_i = []
    datasets_out = []
    datasets_out_o = []
    label = time.strftime("%H:%M:%S", time.localtime())

    try:
        intf = get_ipaddress()
        intf = intf['interface'][0]

        traffic = get_traffic(intf)
    except Exception:
        traffic = 0

    try:
        cookies = request.COOKIES['traffic']
    except Exception:
        cookies = None

    if not cookies:
        datasets_in.append(0)
        datasets_in_i.append(0)
        datasets_out.append(0)
        datasets_out_o.append(0)
    else:
        datasets = json.loads(cookies)
        datasets_in = datasets[0]
        datasets_out = datasets[1]
        datasets_in_i = datasets[2]
        datasets_out_o = datasets[3]

    if len(datasets_in) > 10:
        while datasets_in:
            del datasets_in[0]
            if len(datasets_in) == 10:
                break
    if len(datasets_in_i) > 2:
        while datasets_in_i:
            del datasets_in_i[0]
            if len(datasets_in_i) == 2:
                break
    if len(datasets_out) > 10:
        while datasets_out:
            del datasets_out[0]
            if len(datasets_out) == 10:
                break
    if len(datasets_out_o) > 2:
        while datasets_out_o:
            del datasets_out_o[0]
            if len(datasets_out_o) == 2:
                break

    if len(datasets_in_i) <= 1:
        datasets_in_i.append(float(traffic['traffic_in']))
    if len(datasets_in_i) == 2:
        datasets_in_i.append(float(traffic['traffic_in']))
        del datasets_in_i[0]
    if len(datasets_out_o) <= 1:
        datasets_out_o.append(float(traffic['traffic_out']))
    if len(datasets_out_o) == 2:
        datasets_out_o.append(float(traffic['traffic_out']))
        del datasets_out_o[0]

    dataset_in = (float(((datasets_in_i[1] - datasets_in_i[0]) / 1024) / (time_refresh_net / 1000)))
    dataset_out = (float(((datasets_out_o[1] - datasets_out_o[0]) / 1024) / (time_refresh_net / 1000)))

    if dataset_in > 1024 or dataset_out > 1024:
        dataset_in = (float(dataset_in / 1024))
        dataset_out = (float(dataset_out / 1024))
        label = "MBps"

    if len(datasets_in) <= 9:
        datasets_in.append(dataset_in)
    if len(datasets_in) == 10:
        datasets_in.append(dataset_in)
        del datasets_in[0]
    if len(datasets_out) <= 9:
        datasets_out.append(dataset_out)
    if len(datasets_out) == 10:
        datasets_out.append(dataset_out)
        del datasets_out[0]

    # Some fix division by 0 Chart.js
    if len(datasets_in) == 10:
        if sum(datasets_in) == 0:
            datasets_in[9] += 0.1
        if sum(datasets_in) / 10 == datasets_in[0]:
            datasets_in[9] += 0.1

    traff = {
        'labels': [label] * 10,
        'datasets': [
            {
                "fillColor": "rgba(105,210,231,0.5)",
                "strokeColor": "rgba(105,210,231,1)",
                "pointColor": "rgba(105,210,231,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_in
            },
            {
                "fillColor": "rgba(227,48,81,0.5)",
                "strokeColor": "rgba(227,48,81,1)",
                "pointColor": "rgba(227,48,81,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_out
            }
        ]
    }

    cookie_traffic = [datasets_in, datasets_out, datasets_in_i, datasets_out_o]
    data = json.dumps(traff)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.cookies['traffic'] = cookie_traffic
    response.write(data)
    return response


def getdiskio(request):
    """
    Return the reads and writes for the drive
    """
    datasets_in = []
    datasets_in_i = []
    datasets_out = []
    datasets_out_o = []

    try:
        diskrw = get_disk_rw()
        diskrw = diskrw[0]
    except Exception:
        diskrw = 0

    try:
        cookies = request.COOKIES['diskrw']
    except Exception:
        cookies = None

    if not cookies:
        datasets_in.append(0)
        datasets_in_i.append(0)
        datasets_out.append(0)
        datasets_out_o.append(0)
    else:
        datasets = json.loads(cookies)
        datasets_in = datasets[0]
        datasets_out = datasets[1]
        datasets_in_i = datasets[2]
        datasets_out_o = datasets[3]

    if len(datasets_in) > 10:
        while datasets_in:
            del datasets_in[0]
            if len(datasets_in) == 10:
                break
    if len(datasets_in_i) > 2:
        while datasets_in_i:
            del datasets_in_i[0]
            if len(datasets_in_i) == 2:
                break
    if len(datasets_out) > 10:
        while datasets_out:
            del datasets_out[0]
            if len(datasets_out) == 10:
                break
    if len(datasets_out_o) > 2:
        while datasets_out_o:
            del datasets_out_o[0]
            if len(datasets_out_o) == 2:
                break

    if len(datasets_in_i) <= 1:
        datasets_in_i.append(int(diskrw[1]))
    if len(datasets_in_i) == 2:
        datasets_in_i.append(int(diskrw[1]))
        del datasets_in_i[0]
    if len(datasets_out_o) <= 1:
        datasets_out_o.append(int(diskrw[2]))
    if len(datasets_out_o) == 2:
        datasets_out_o.append(int(diskrw[2]))
        del datasets_out_o[0]

    dataset_in = (int((datasets_in_i[1] - datasets_in_i[0]) / (time_refresh_net / 1000)))
    dataset_out = (int((datasets_out_o[1] - datasets_out_o[0]) / (time_refresh_net / 1000)))

    if len(datasets_in) <= 9:
        datasets_in.append(dataset_in)
    if len(datasets_in) == 10:
        datasets_in.append(dataset_in)
        del datasets_in[0]
    if len(datasets_out) <= 9:
        datasets_out.append(dataset_out)
    if len(datasets_out) == 10:
        datasets_out.append(dataset_out)
        del datasets_out[0]

    # Some fix division by 0 Chart.js
    if len(datasets_in) == 10:
        if sum(datasets_in) == 0:
            datasets_in[9] += 0.1
        if sum(datasets_in) / 10 == datasets_in[0]:
            datasets_in[9] += 0.1

    disk_rw = {
        'labels': [""] * 10,
        'datasets': [
            {
                "fillColor": "rgba(245,134,15,0.5)",
                "strokeColor": "rgba(245,134,15,1)",
                "pointColor": "rgba(245,134,15,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_in
            },
            {
                "fillColor": "rgba(15,103,245,0.5)",
                "strokeColor": "rgba(15,103,245,1)",
                "pointColor": "rgba(15,103,245,1)",
                "pointStrokeColor": "#fff",
                "data": datasets_out
            }
        ]
    }

    cookie_diskrw = [datasets_in, datasets_out, datasets_in_i, datasets_out_o]
    data = json.dumps(disk_rw)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.cookies['diskrw'] = cookie_diskrw
    response.write(data)
    return response
    



def chunks(get, n):
    return [get[i:i + n] for i in range(0, len(get), n)]


def get_uptime():
    """
    Get uptime
    """
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_time = str(timedelta(seconds=uptime_seconds))
            data = uptime_time.split('.', 1)[0]

    except Exception as err:
        data = str(err)

    return data


def get_ipaddress():
    """
    Get the IP Address
    """
    data = []
    try:
        eth = os.popen("ip addr | grep LOWER_UP | awk '{print $2}'")
        iface = eth.read().strip().replace(':', '').split('\n')
        eth.close()
        del iface[0]

        for i in iface:
            pipe = os.popen("ip addr show " + i + "| awk '{if ($2 == \"forever\"){!$2} else {print $2}}'")
            data1 = pipe.read().strip().split('\n')
            pipe.close()
            if len(data1) == 2:
                data1.append('unavailable')
            if len(data1) == 3:
                data1.append('unavailable')
            data1[0] = i
            data.append(data1)

        ips = {'interface': iface, 'itfip': data}

        data = ips

    except Exception as err:
        data = str(err)

    return data


def get_cpus():
    """
    Get the number of CPUs and model/type
    """
    try:
        pipe = os.popen("cat /proc/cpuinfo |" + "grep 'model name'")
        data = pipe.read().strip().split(':')[-1]
        pipe.close()

        if not data:
            pipe = os.popen("cat /proc/cpuinfo |" + "grep 'Processor'")
            data = pipe.read().strip().split(':')[-1]
            pipe.close()

        cpus = multiprocessing.cpu_count()

        data = {'cpus': cpus, 'type': data}

    except Exception as err:
        data = str(err)

    return data


def get_users():
    """
    Get the current logged in users
    """
    try:
        pipe = os.popen("who |" + "awk '{print $1, $2, $6}'")
        data = pipe.read().strip().split('\n')
        pipe.close()

        if data == [""]:
            data = None
        else:
            data = [i.split(None, 3) for i in data]

    except Exception as err:
        data = str(err)

    return data


def get_traffic(request):
    """
    Get the traffic for the specified interface
    """
    try:
        pipe = os.popen("cat /proc/net/dev |" + "grep " + request + "| awk '{print $1, $9}'")
        data = pipe.read().strip().split(':', 1)[-1]
        pipe.close()

        if not data[0].isdigit():
            pipe = os.popen("cat /proc/net/dev |" + "grep " + request + "| awk '{print $2, $10}'")
            data = pipe.read().strip().split(':', 1)[-1]
            pipe.close()

        data = data.split()

        traffic_in = int(data[0])
        traffic_out = int(data[1])

        all_traffic = {'traffic_in': traffic_in, 'traffic_out': traffic_out}

        data = all_traffic

    except Exception as err:
        data = str(err)

    return data

def get_disk():
    """
    Get disk usage
    """
    try:
        pipe = os.popen("df -Ph | " + "grep -v Filesystem | " + "awk '{print $1, $2, $3, $4, $5, $6}'")
        data = pipe.read().strip().split('\n')
        pipe.close()

        data = [i.split(None, 6) for i in data]

    except Exception as err:
        data = str(err)

    return data


def get_disk_rw():
    """
    Get the disk reads and writes
    """
    try:
        pipe = os.popen("cat /proc/partitions | grep -v 'major' | awk '{print $4}'")
        data = pipe.read().strip().split('\n')
        pipe.close()

        rws = []
        for i in data:
            if i.isalpha():
                pipe = os.popen("cat /proc/diskstats | grep -w '" + i + "'|awk '{print $4, $8}'")
                rw = pipe.read().strip().split()
                pipe.close()

                rws.append([i, rw[0], rw[1]])

        if not rws:
            pipe = os.popen("cat /proc/diskstats | grep -w '" + data[0] + "'|awk '{print $4, $8}'")
            rw = pipe.read().strip().split()
            pipe.close()

            rws.append([data[0], rw[0], rw[1]])

        data = rws

    except Exception as err:
        data = str(err)

    return data


def get_mem():
    """
    Get memory usage
    """
    try:
        pipe = os.popen(
            "free -tm | " + "grep 'Mem' | " + "awk '{print $2,$4,$6,$7}'")
        data = pipe.read().strip().split()
        pipe.close()

        allmem = int(data[0])
        freemem = int(data[1])
        buffers = int(data[2])
        availamem = int(data[3])


        percent = (100 - ((availamem * 100) / allmem))
        usage = (allmem - availamem)

        mem_usage = {'usage': usage, 'buffers': buffers, 'freemem': freemem, 'availamem': availamem, 'percent': percent}

        data = mem_usage

    except Exception as err:
        data = str(err)

    return data

def get_cpu_usage():
    """
    Get the CPU usage and running processes
    """
    try:
        pipe = os.popen("ps aux --sort -%cpu,-rss")
        data = pipe.read().strip().split('\n')
        pipe.close()

        usage = [i.split(None, 10) for i in data]
        del usage[0]

        total_usage = []

        for element in usage:
            usage_cpu = element[2]
            total_usage.append(usage_cpu)

        total_usage = sum(float(i) for i in total_usage)

        total_free = ((100 * int(get_cpus()['cpus'])) - float(total_usage))

        cpu_used = {'free': total_free, 'used': float(total_usage), 'all': usage}

        data = cpu_used

    except Exception as err:
        data = str(err)

    return data


def get_load():
    """
    Get load average
    """
    try:
        data = os.getloadavg()[0]
    except Exception as err:
        data = str(err)

    return data


def get_netstat():
    """
    Get ports and applications
    """
    try:
        pipe = os.popen(
            "ss -tnp | grep ESTAB | awk '{print $4, $5}'| sed 's/::ffff://g' | awk -F: '{print $1, $2}' "
            "| awk 'NF > 0' | sort -n | uniq -c")
        data = pipe.read().strip().split('\n')
        pipe.close()

        data = [i.split(None, 4) for i in data]

    except Exception as err:
        data = str(err)

    return data


def getall(request):
    return render_to_response('main.html', {'time_refresh': time_refresh,
                                            'time_refresh_long': time_refresh_long,
                                            'time_refresh_net': time_refresh_net,
                                                    }, context_instance=RequestContext(request))

def monitor_host(request,id):
    obj = Information.objects.filter(id=id)[0]
    ret = {}
    if obj:
        ip = obj.privateip
    ret = {'ip':ip}
    return render (request,'ajax_demo.html',{'ip':ip})
@csrf_exempt
def ajax_demo(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        print ip
        ret = {}
        #ret = {'ip':ip}
        if ip:
            ret = {'ip':ip}
        return  HttpResponse(json.dumps(ret))
    else:
        ret = {'ip':'1.2.2.3'}
        return  HttpResponse(json.dumps(ret))
        
@csrf_exempt
def ajaxtest(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        MetricObj = ServerDisk.objects.filter(ip = ip).order_by('-id')[0]
        if MetricObj:
        #ret = {'status':MetricObj.disk}
        #for i in MetricObj:
            ret ={'disk':MetricObj.disk }
        else:
            ret = {'disk':'0'}
        return HttpResponse(json.dumps(ret))
    else:
        print request.method 
@csrf_exempt
def ajaxtestcpu(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        MetricObj = ServerCpu.objects.filter(ip = ip).order_by('-id')[0]
        if MetricObj:
            ret ={"list":[{"type":'usage_cpu',"value":MetricObj.usage_cpu },{"type":'idle_cpu',"value":MetricObj.idle_cpu }]}
            #print ret
        else:
            ret ={"list":[{"type":'usage_cpu',"value":'0' },{"type":'idle_cpu',"value":'0' }]}
        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(request.method+"方法")
        
@csrf_exempt
def ajaxtestmem(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        ret = {}
        MetricObj = ServerMem.objects.filter(ip = ip).order_by('-id')[0]
        if MetricObj:
            ret ={"mem_total":MetricObj.mem_total,"mem_used":MetricObj.mem_used,'datatime':MetricObj.datatime,\
           "swap_total":MetricObj.swap_total,"swap_used":MetricObj.swap_used,"percent": MetricObj.mem_use_percent}
            #print ret
        else:
            ret = {"mem_total":'0' ,"mem_used":'0' ,'datatime':'0' , "swap_total":'0' ,"swap_used":'0' ,"percent": '0' }
        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(request.method+"方法")

@csrf_exempt
def ajaxtestnet(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        MetricObj = ServerNet.objects.filter(ip = ip).order_by('-id')[0]
        MetricObj1 = ServerNet.objects.filter(ip = ip).order_by('-id')[1]
        traffic_in = ''
        traffic_out = ''
        ret = {}
        if MetricObj and MetricObj1:
            traffic_in = (int(MetricObj.traffic_in) - int(MetricObj1.traffic_in))/2
            traffic_out = (int(MetricObj.traffic_out) - int(MetricObj1.traffic_out))/2
            ret = {'datatime':MetricObj.datatime, 'traffic_in':traffic_in, 'traffic_out':traffic_out, 'interface':MetricObj.iface }
            #print ret
        else:
            ret = {'datatime':'0', 'traffic_in':'0', 'traffic_out':'0', 'interface':'0' }
        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(request.method+"方法")

@csrf_exempt
def ajaxtestdisk_io(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        #print ip
        MetricObj = ServerDisk_io.objects.filter(ip =ip).order_by('-id')[0]
        #print MetricObj.r_io
        MetricObj1 = ServerDisk_io.objects.filter(ip = ip).order_by('-id')[1]
        #print MetricObj1.r_io
        r_io = ''
        w_io = ''
        ret = {}
        if MetricObj and MetricObj1:
            r_io = (int(MetricObj.r_io) - int(MetricObj1.r_io))/2
            w_io = (int(MetricObj.w_io) - int(MetricObj1.w_io))/2
            ret = {'datatime':MetricObj.datatime, 'r_io':r_io, 'w_io':w_io, 'device':MetricObj.dev}
             #print ret
        else:
            ret = {'datatime':'0', 'r_io':'0', 'w_io':'0', 'device':'0'}
        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(request.method+"方法")
        
@csrf_exempt 
def ajaxtestload_avg(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        MetricObj = ServerBaseMetric.objects.filter(ip = ip).order_by('-id')[0]
        ret = []
        if MetricObj:
            ret = {'datatime':MetricObj.datatime,'load':MetricObj.cpu_load}
        else:
            ret = {'datatime':'0','load':'0'}
        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponse(request.method+'方法')      
        '''
        如何进行数据库选取数据填充到列表，然后进行升序培训。
def ajaxtestload_avg(request):
    if request.method == 'POST':
        MetricObj = ServerBaseMetric.objects.filter(ip = '172.18.78.74').order_by('-id')[0:4]
        ret = []
        if MetricObj:
            for i in  MetricObj:
                ret.append({'datatime':i.datatime,'load':i.cpu_load})   
            ret0 = ret[:]
            foo = lambda s:s['datatime']
            ret0.sort(key=foo)                    
        return HttpResponse(json.dumps(ret0))
    else:
        print  request.method
        return HttpResponse('123')    
'''        
@csrf_exempt
def monitor_metric_writedb(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        ip=req['ip']
        uptime = req['uptime']
        cpu_load = req['load']
        cputype = req['cpus']
        platform = req['platform']
        hostname = platform['hostname']
        kernel = platform['kernel']
        osname = platform['osname']
        getcpu = req['cpu_usage']
        usage_cpu = getcpu['usage_cpu']
        idle_cpu =  getcpu['idle_cpu']
        datatime = req['time_now']
        disk =req['disk']
        getmem = req['mem']
        swap_total = getmem['swap_total']
        swap_used = getmem['swap_used']
        swap_free = getmem['swap_free']
        mem_total = getmem['total']
        mem_used = getmem['usage']
        mem_free = getmem['free']
        mem_buff = getmem['buff']
        mem_used_percent = getmem['percent']
        net = req['traffic']
        iface = net[0]['interface']
        traffic_in =net[0]['traffic_in']
        traffic_out = net[0]['traffic_out']
        disk_io = req['disk_rw']
        dev = disk_io['device']
        r_io = disk_io['r_io']
        w_io = disk_io['w_io']
       # print w_io
        historybaseobj = ServerBaseMetric(
                                        ip=ip,\
                                        uptime=uptime,\
                                        cpu_load=cpu_load,\
                                        cputype=cputype,\
                                        hostname=hostname,\
                                        kernel=kernel,\
                                        datatime = datatime,\
                                        osname=osname                                      
                                        )
        historycpuobj = ServerCpu(
                                        ip =ip,\
                                        usage_cpu = usage_cpu,\
                                        idle_cpu = idle_cpu
                                        )
        historydiskobj = ServerDisk(
                                        ip =ip,\
                                        datatime = datatime,\
                                        disk = json.dumps(disk)
                                        )
        historymemobj = ServerMem(
                                        ip =ip,\
                                        datatime = datatime,\
                                        swap_total = swap_total,\
                                        swap_used = swap_used,\
                                        mem_total = mem_total,\
                                        mem_used =mem_used,\
                                        swap_free =swap_free,\
                                        mem_free =mem_free,\
                                        mem_buff = mem_buff,\
                                        mem_use_percent = mem_used_percent
        )
        historynetobj = ServerNet(
                                        ip =ip,\
                                        datatime = datatime,\
                                        iface = iface,\
                                        traffic_in = traffic_in,\
                                        traffic_out =traffic_out
        )
        historydiskioobj = ServerDisk_io(
                                        ip =ip,\
                                        datatime = datatime,\
                                        dev = dev,\
                                        r_io = r_io,\
                                        w_io = w_io
        )
        try:
            historybaseobj.save()
            historycpuobj.save()
            historydiskobj.save()
            historymemobj.save()
            historynetobj.save()
            historydiskioobj.save()
        except Exception,e:
            return HttpResponse("入库失败，请与管理员联系！"+str(e))
        Response_result="OK"
        return HttpResponse(Response_result)
    else:
        return HttpResponse("非法提交！")
   