import commands
from weather import *
area=commands.getoutput('sh /home/zqxt_form2/monitor/ip.sh 2>/dev/null')
get(area)
