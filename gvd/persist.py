# This file is placed in the Public Domain.
#
#


"eternity"


import datetime
import os
import _thread


from opd.objects import fqn, items, load
from opd.parsers import spl


lock = _thread.allocate_lock()


def ident(obj):
    return os.path.join(
                        fqn(obj),
                        os.path.join(*str(datetime.datetime.now()).split())
                       )


def fetch(obj, pth):
    pth2 = store(pth)
    read(obj, pth2)
    return strip(pth)


def read(obj, pth):
    with lock:
        with open(pth, 'r', encoding='utf-8') as ofile:
            update(obj, load(ofile))


def search(obj, selector):
    res = False
    if not selector:
        return True
    for key, value in items(selector):
        if key not in obj:
            res = False
            break
        for vval in spl(str(value)):
            val = getattr(obj, key, None)
            if str(vval).lower() in str(val).lower():
                res = True
            else:
                res = False
                break
    return res


def sync(obj, pth=None):
    if pth is None:
        pth = ident(obj)
    pth2 = store(pth)
    write(obj, pth2)
    return pth


def write(obj, pth):
    with lock:
        cdir(os.path.dirname(pth))
        with open(pth, 'w', encoding='utf-8') as ofile:
            dump(obj, ofile, indent=4)
