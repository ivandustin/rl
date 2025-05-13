def ppop(iq, oq):
    def wrapper(state):
        iq.put(state)
        return oq.get()

    return wrapper
