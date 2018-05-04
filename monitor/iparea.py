# -*- coding: utf-8 -*-
import requests
import sys
 
def checkip(ip):
 
  URL = 'http://ip.taobao.com/service/getIpInfo.php'
  try:
    r = requests.get(URL, params=ip, timeout=5)
  except requests.RequestException as e:
    print(e)
  else:
    json_data = r.json()
    if json_data[u'code'] == 0:
    #  print '所在国家： ' + json_data[u'data'][u'country'].encode('utf-8')
    #  print '所在地区： ' + json_data[u'data'][u'area'].encode('utf-8')
    #  print '所在省份： ' + json_data[u'data'][u'region'].encode('utf-8')
    #  print '所在城市： ' + json_data[u'data'][u'city'].encode('utf-8')
      print json_data[u'data'][u'city'].encode('utf-8')
    #  print '所属运营商：' + json_data[u'data'][u'isp'].encode('utf-8')
    else:
      print '查询失败,请稍后再试！'
localip=sys.argv[1]
checkip({'ip':localip})
