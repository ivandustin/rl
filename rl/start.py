from collections import deque
from queue import Queue
from .thread import thread
from .gput import gput
from .ppop import ppop
from .work import work


def start(n: int, m: int, init, stop, ask, apply, no, yes, learn):
    yq, nq, qq = deque(maxlen=m), deque(maxlen=m), deque(maxlen=m)
    iqs = [Queue() for _ in range(n)]
    oqs = [Queue() for _ in range(n)]
    for iq, oq in zip(iqs, oqs):
        askfn = ppop(iq, oq)
        thread(work)(yq, nq, qq, init, stop, askfn, apply, no, yes)
    while True:
        gput(ask, iqs, oqs)
        learn(list(yq), list(nq), list(qq))
