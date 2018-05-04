#!/bin/bash
ansible -s  $1  -m shell -a "cat /proc/loadavg"
