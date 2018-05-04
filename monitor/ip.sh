#!/bin/bash
ip=`curl http://members.3322.org/dyndns/getip` 


python /var/Django_Linux/zqxt_form2/monitor/iparea.py $ip |tee ip.txt
