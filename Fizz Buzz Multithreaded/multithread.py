# Oscar Yu
# Threading Test

import threading
counter = 0
max = counter
countLock = threading.Lock()
aCount = 0
bCount = 0

def aCounter():
    print("hello a")
    global counter, aCount
    while counter < 100:
        countLock.acquire()
        counter += 1
        aCount += 1
        print(f"aCounter++: {counter}")
        countLock.release()

def bCounter():
    print("hello b")
    global counter, bCount
    while counter < 100:
        countLock.acquire()
        counter += 1
        bCount += 1
        print(f"bCounter++: {counter}")
        countLock.release()

threadA = threading.Thread(target=aCounter, args=())
threadB = threading.Thread(target=bCounter, args=())
threadA.start()
threadB.start()

while counter < 100:
    None
else:
    print(aCount, bCount)