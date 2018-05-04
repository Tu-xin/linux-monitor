#!/bin/bash
dir="/home/zqxt_form2/monitor"
sh ${dir}/cpu.sh $1 |tail -n 1|awk '{print $1}'
