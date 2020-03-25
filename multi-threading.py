import clearterm
from threading import Thread
from time import sleep


class Hello(Thread):  # applying thread
    def run(self):
        for _ in range(1, 6):
            sleep(1)
            print('Hello')


class Hi(Thread):
    def run(self):
        for _ in range(1, 6):
            sleep(1)
            print('Hi')


h1 = Hello(target='run')
h2 = Hi(target='run')
h1.start()
sleep(0.5)
h2.start()
h1.join()
h2.join()

print('Bye')
