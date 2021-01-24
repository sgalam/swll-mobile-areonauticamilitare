# -*- coding: utf-8 -*-

import signal
import time


class Loop(object):

    active = True

    def __init__(self):
        signal.signal(signal.SIGINT, self.terminate)
        signal.signal(signal.SIGQUIT, self.terminate)
        signal.signal(signal.SIGTERM, self.terminate)

    def terminate(self, signum, frame):

        print("intercettato segnale %s, termino" % signum)
        self.active = False

    def __call__(self):
        while self.active:
            time.sleep(1)


if __name__ == "__main__":
    Loop()()
