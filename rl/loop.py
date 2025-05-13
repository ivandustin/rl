from .exceptions import No, Yes


def loop(init, stop, ask, apply, no, yes):
    state = init()
    while not stop(state):
        action = ask(state)
        next = apply(action, state)
        if no(action, state, next):
            raise No(state, action)
        if yes(action, state, next):
            raise Yes(state, action)
        yield state, action
        state = next
