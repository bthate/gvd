# This file is placed in the Public Domain.
#
# pylint: disable=C0116,W0105,E0402


"running threads"


import threading
import time


from ..objects import Object
from ..methods import update
from ..threads import laps


def __dir__():
    return (
            "thr",
           )


STARTTIME = time.time()


def thr(event):
    result = []
    for thread in sorted(threading.enumerate(), key=lambda x: x.name):
        if str(thread).startswith('<_'):
            continue
        obj = Object()
        update(obj, vars(thread))
        if getattr(obj, 'sleep', None):
            uptime = obj.sleep - int(time.time() - obj.state.latest)
        elif getattr(obj, 'starttime', None):
            uptime = int(time.time() - obj.starttime)
        else:
            uptime = int(time.time() - STARTTIME)
        result.append((uptime, thread.name))
    res = []
    for uptime, txt in sorted(result, key=lambda x: x[1]):
        lap = laps(uptime)
        res.append(f'{txt}/{lap}')
    if res:
        event.reply(' '.join(res))
    else:
        event.reply('no threads')
