#!/bin/bash
minute1="`date --date '1 minute ago ' +%s`"
minute3="`date --date '3 minute ago ' +%s`"
minute5="`date --date '5 minute ago ' +%s`"

dir="/home/zqxt_form2/monitor/rrdtool/"
rrdtool graph ${dir}/cpu1.jpg --step 5 -s ${minute1} -t "cpu free  monitor (1 minute)" -v cpu DEF:cpu=${dir}/cpu.rrd:cpuds:AVERAGE LINE1:cpu#FF0000:'cpu free'
rrdtool graph ${dir}/cpu3.jpg --step 5 -s ${minute3} -t "cpu free  monitor (3 minute" -v cpu DEF:cpu=${dir}/cpu.rrd:cpuds:AVERAGE LINE1:cpu#FF0000:'cpu free'
rrdtool graph ${dir}/cpu5.jpg --step 5 -s ${minute5} -t "cpu free monitor (5 minute)" -v cpu DEF:cpu=${dir}/cpu.rrd:cpuds:AVERAGE LINE1:cpu#FF0000:'cpu free'

rrdtool graph ${dir}/memory1.jpg --step 5 -s ${minute1} -t " memory free monitor (1 minute) " -v cpu DEF:cpu=${dir}/memory.rrd:memoryds:AVERAGE LINE1:cpu#FF0000:'memory free(MB)'
rrdtool graph ${dir}/memory3.jpg --step 5 -s ${minute3} -t " memory free monitor (3 minute)" -v cpu DEF:cpu=${dir}/memory.rrd:memoryds:AVERAGE LINE1:cpu#FF0000:'memory free(MB)'
rrdtool graph ${dir}/memory5.jpg --step 5 -s ${minute5} -t " memory free monitor (5 minute)" -v cpu DEF:cpu=${dir}/memory.rrd:memoryds:AVERAGE LINE1:cpu#FF0000:'memory free(MB)'

rrdtool graph ${dir}/disk1.jpg --step 5 -s ${minute1} -t "disk used /   monitor (1 minute)" -v cpu DEF:cpu=${dir}/disk.rrd:diskds:AVERAGE LINE1:cpu#FF0000:'disk free %'
rrdtool graph ${dir}/disk3.jpg --step 5 -s ${minute3} -t "disk used /   monitor (3 minute)" -v cpu DEF:cpu=${dir}/disk.rrd:diskds:AVERAGE LINE1:cpu#FF0000:'disk free %'
rrdtool graph ${dir}/disk5.jpg --step 5 -s ${minute5} -t "disk used /   monitor (5 minute)" -v cpu DEF:cpu=${dir}/disk.rrd:diskds:AVERAGE LINE1:cpu#FF0000:'disk free %'
dir2="/home/zqxt_form2/monitor/static/jpg/monitor/"
cp -rf ${dir}/cpu1.jpg ${dir2}
cp -rf ${dir}/cpu3.jpg ${dir2}
cp -rf ${dir}/cpu5.jpg ${dir2}
cp -rf ${dir}/memory1.jpg ${dir2}
cp -rf ${dir}/memory3.jpg ${dir2}
cp -rf ${dir}/memory5.jpg ${dir2}
cp -rf ${dir}/disk1.jpg ${dir2}
cp -rf ${dir}/disk3.jpg ${dir2}
cp -rf ${dir}/disk5.jpg ${dir2}

