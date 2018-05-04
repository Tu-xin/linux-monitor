"""Linux_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^index/$', 'Login.views.index',name='index'),
    url(r'^main/$', 'monitor.views.getall', name='main'),
    url(r'^info/memory/$', 'monitor.views.memusage', name='memusage'),
    url(r'^info/uptime/$', 'monitor.views.uptime', name='uptime'),
    url(r'^info/cpuusage/$', 'monitor.views.cpuusage', name='cpuusage'),
    url(r'^info/getdisk/$', 'monitor.views.getdisk', name='getdisk'),
    url(r'^info/getusers/$', 'monitor.views.getusers', name='getusers'),
    url(r'^info/getips/$', 'monitor.views.getips', name='getips'),
    url(r'^info/gettraffic/$', 'monitor.views.gettraffic', name='gettraffic'),
    url(r'^info/proc/$', 'monitor.views.getproc', name='getproc'),
    url(r'^info/getdiskio/$', 'monitor.views.getdiskio', name='getdiskio'),
    url(r'^info/loadaverage/$', 'monitor.views.loadaverage', name='loadaverage'),
    url(r'^info/platform/([\w\-\.]+)/$', 'monitor.views.platform', name='platform'),
    url(r'^info/getcpus/([\w\-\.]+)/$', 'monitor.views.getcpus', name='getcpus'),
    url(r'^info/getnetstat/$', 'monitor.views.getnetstat', name='getnetstat'),
    url(r'^ajax_demo/$','monitor.views.ajax_demo'),
    url(r'^logout/$', 'Login.views.logout'),
    url(r'^login/$', 'Login.views.Login'),
    url(r'^register/$', 'Login.views.register'),
    url(r'^deluser/$', 'Login.views.deluser'),
    url(r'^cmdb/', 'cmdb.views.infor'),
    url(r'^server/', 'monitor.views.server'),
    #url(r'^monitor/cpu/', 'monitor.views.cpu'),
    url(r'^monitorset/$', 'monitor.views.monitorset'),
    url(r'^servers/$', 'monitor.views.servers'),
    url(r'^filersync/$', 'monitor.views.filersync'),
    url(r'^program/$', 'monitor.views.program'),
    url(r'^servicemanage/$', 'monitor.views.servicemanage'),
    url(r'^linuxlog/$', 'monitor.views.linuxlog'),
    url(r'^servicelog/$', 'monitor.views.servicelog'),
#url(r'^questions/$', 'monitor.views.Questions'),
    url(r'^Experience/$', 'monitor.views.experience'),
    url(r'^monitort/$', 'monitor.views.monitort'),
    url(r'^webssh/$', 'monitor.views.websshtest'),
    #url(r'^monitor/showdisk/$', 'monitor.views.showdisk'),
    url(r'^monitor/memory/', 'monitor.views.memory'),
    url(r'^monitor/disk/', 'monitor.views.disk'),
    url(r'^monitor_host/(?P<id>[0-9]+)/$', 'monitor.views.monitor_host',name='monitor_host'),
    url(r'^ajax/getdisk/$','monitor.views.ajaxtest'),
    url(r'^ajax/getcpu/$','monitor.views.ajaxtestcpu'),
    url(r'^ajax/getcpu_load/$','monitor.views.ajaxtestload_avg'),
    url(r'^ajax/getmem/$','monitor.views.ajaxtestmem'),
    url(r'^ajax/getnet/$','monitor.views.ajaxtestnet'),
    url(r'^ajax/getdisk_io/$','monitor.views.ajaxtestdisk_io'),
    url(r'^monitor_metric_writedb/$','monitor.views.monitor_metric_writedb'),
    url(r'^admin/', include(admin.site.urls)),
    
]
