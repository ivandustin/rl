from threading import Thread


def thread(function):
    def wrapper(*args):
        thread = Thread(target=function, args=args, daemon=True)
        thread.start()

    return wrapper
