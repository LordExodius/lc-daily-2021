# Oscar Yu
# June 12th, 2021

import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroLock = threading.Lock()
        self.evenLock = threading.Lock()
        self.evenLock.acquire()
        self.oddLock = threading.Lock()
        self.oddLock.acquire()
        
        self.output = ""
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zeroLock.acquire()
            if not i % 2:
                self.evenLock.release()
            else:
                self.oddLock.release()
            printNumber(0)
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.evenLock.acquire()
            printNumber(i)
            self.zeroLock.release()
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddLock.acquire()
            printNumber(i)
            self.zeroLock.release()
        
        