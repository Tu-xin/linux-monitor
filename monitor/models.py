#coding:utf-8
from django.db import models
class monitors(models.Model):
    servername = models.CharField(max_length=30)
    item = models.CharField(max_length=30)
    value = models.CharField(max_length=30,default="")
    serverip = models.GenericIPAddressField()
    time = models.DateTimeField()
    def __unicode__(self):
        return self.servername


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username
'''
class question(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField()
    '''

class Experience(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField()

class zaj(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
class ServerBaseMetric(models.Model):
    id = models.AutoField(primary_key=True) # Field name made lowercase.
    ip = models.GenericIPAddressField()
    hostname = models.CharField(max_length=20)
    cpu_load = models.CharField(max_length=5)
    kernel = models.CharField(max_length=30)
    osname = models.CharField(max_length=40)
    uptime = models.CharField(max_length=20)
    cputype =  models.CharField(max_length=50)
    datatime = models.CharField(max_length=20,default='null')
    class Meta:
        db_table = u'server_metric'
 
class ServerCpu(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    usage_cpu = models.CharField(max_length=30)
    idle_cpu = models.CharField(max_length=30)
    class Meta:
        db_table = u'cpu_metric'

class ServerDisk(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    datatime = models.CharField(max_length=20,default='null')
    disk = models.CharField(max_length=400)
    class Meta:
        db_table = u'disk_metric'
    
class ServerMem(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    swap_total = models.CharField(max_length=10)
    swap_used = models.CharField(max_length=10)
    swap_free = models.CharField(max_length=10)
    mem_total = models.CharField(max_length=10)
    mem_used = models.CharField(max_length=10)
    mem_free = models.CharField(max_length=10)
    mem_buff = models.CharField(max_length=10)
    mem_use_percent = models.CharField(max_length=10)
    datatime = models.CharField(max_length=20,default='0')
    class Meta:
        db_table = u'mem_metric'

class ServerNet(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    iface = models.CharField(max_length=10)
    traffic_in = models.CharField(max_length=10)
    traffic_out = models.CharField(max_length=10)
    datatime = models.CharField(max_length=20,default='0')
    class Meta:
        db_table = u'net_metric'

class ServerDisk_io(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.GenericIPAddressField()
    dev = models.CharField(max_length=10)
    r_io = models.CharField(max_length=10)
    w_io = models.CharField(max_length=10)
    datatime = models.CharField(max_length=20,default='0')
    class Meta:
        db_table = u'disk_io_metric'

