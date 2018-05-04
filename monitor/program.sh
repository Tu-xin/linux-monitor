#!/bin/bash
ansible $1 -m service -a "name=$2 state=$3 enabled=yes"
