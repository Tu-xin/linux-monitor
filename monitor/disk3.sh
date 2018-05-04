#!/bin/bash
sh  /home/zqxt_form2/monitor/disk2.sh $1 |grep 'stdout":' |awk '{print $2}' |awk -F '%' '{print $1}'|awk -F '\"' '{print $2}' 
