#!/urs/bin/env python
import platform

try:
    osname = " ".join(platform.linux_distribution())
    uname = platform.uname()
    if osname == ' ':
        osname = uname[0]
    
    data = {'osname': osname, 'hostname': uname[1], 'kernel': uname[2]}
except Exception as err:
    data = str(err)

print  data
