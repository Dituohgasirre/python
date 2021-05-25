from subprocess import getstatusoutput

from django.shortcuts import render
from django.http import HttpResponse


def get_cpu_info():
    cmd = 'uptime'
    status, out = getstatusoutput(cmd)
    if status != 0:
        return None
    texts = out.split()[-3:]
    values = [float(x.strip(',')) for x in texts]
    msg = 'CPU: '
    msg += '1min: %s' % values[0]
    msg += ', 5min: %s' % values[1]
    msg += ', 15min: %s' % values[2]
    return msg


def get_ram_info():
    cmd = 'free -b'
    status, out = getstatusoutput(cmd)
    if status != 0:
        return None
    texts = out.splitlines()[1].split()[-6:]
    values = [int(x) for x in texts]
    names = ['total', 'used', 'free', 'shared', 'buffers', 'cached']
    items = dict(zip(names, values))
    msg = 'CPU: ' + ','.join(['%s:%s' % x for x in items.items()])
    return msg


def sysinfo(request, task):
    if task == 'cpu':
        msg = get_cpu_info()
    elif task == 'ram':
        msg = get_ram_info()
    else:
        msg = 'task "%s" not supported' % task
    return HttpResponse(msg)
