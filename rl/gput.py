def gput(fn, iqs, oqs):
    ins = [q.get() for q in iqs]
    outs = fn(ins)
    for o, q in zip(outs, oqs):
        q.put(o)
