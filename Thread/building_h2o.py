import threading


class H2O:
    def __init__(self):
        self.hnum = 0
        self.onum = 0
        self.c = threading.Condition()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hnum += 1
        if self.hnum == 2:
            with self.c:
                self.c.wait_for(lambda: self.onum == 1)
                self.hnum = 0
                self.onum = 0
                self.notify_all()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.onum += 1
        with self.c:
            self.c.wait_for(lambda: self.hnum == 0 and self.onum == 0)
            self.notify_all()