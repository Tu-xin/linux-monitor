# coding:utf-8
import urllib2    
import json 
import sys
cityList_main = [    
    {'code':"101010100", 'name':"北京"},
    {'code':"101180201", 'name':"安阳"},
]
def get_weather(d):  
    url = 'http://www.weather.com.cn/data/sk/'+d+'.html'  
    weatherHtml = urllib2.urlopen(url).read()    
    weatherJSON = json.JSONDecoder().decode(weatherHtml)  
    weatherInfo = weatherJSON['weatherinfo']  
    return weatherInfo  


#通过城市名获得城市代码，并调用get_weather获得天气信息  
def city_weather_info(cityname):  
    for value in cityList_main:  
        if value['name']==cityname:  
            code = value['code']  
            break  
    return get_weather(code)  
  
#打印某个城市的天气信息  
def print_weather_info(cityname):  
    info = city_weather_info(cityname)  
    #print u"城市:",info['city']  
    #print u"时实温度:",info['temp']  
    print info['temp']  
   # print u"风向:",info['WD']  
   # print u"风级数:",info['WS']  
   # print u"湿度:",info['SD']  
    #print u"天气发布时间",info['time']  
      
def get(a):  
    print_weather_info(a)  
#city=sys.argv[1]
get('北京')  



