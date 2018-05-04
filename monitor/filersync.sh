#!/bin/bash
ansible  $1  -m copy  -a "src=$2    dest=$3"
