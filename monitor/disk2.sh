#!/bin/bash
ansible -s $1 -m script  -a "/home/zqxt_form2/monitor/disk.sh"
