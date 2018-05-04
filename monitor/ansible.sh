#!/bin/bash
ansible  $1 -m $2  -a "sudo su - '$3' -c '$4'"
