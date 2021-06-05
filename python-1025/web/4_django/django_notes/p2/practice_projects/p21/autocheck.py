import os
import sys

import django


def make_log():
    text = 'all is well'
    pid = os.getpid()
    uid = os.getuid()
    gid = os.getgid()
    log = models.Log(text=text, pid=pid, uid=uid, gid=gid)
    log.save()


if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    dir = os.path.join(dir, 'db')
    sys.path.insert(0, dir)
    settings_mod_path = 'db.p21.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_mod_path)
    django.setup()
    from store import models
    make_log()
