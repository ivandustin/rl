from .exceptions import No, Yes


def loop(module):
    state = module.init()
    while not module.stop(state):
        action = module.ask(state)
        next = module.apply(action, state)
        if module.no(action, state, next):
            raise No(state, action)
        if module.yes(action, state, next):
            raise Yes(state, action)
        yield state, action
        state = next
