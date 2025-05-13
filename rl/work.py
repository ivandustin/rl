from rl.exceptions import End, Yes, No
from rl.loop import loop


def work(yq, nq, qq, init, stop, ask, apply, no, yes):
    while True:
        try:
            for item in loop(init, stop, ask, apply, no, yes):
                qq.append(item)
        except End as e:
            item = e.args
            if isinstance(e, Yes):
                yq.append(item)
            elif isinstance(e, No):
                nq.append(item)
            else:
                assert False
