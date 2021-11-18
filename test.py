import time
import network

sta_if = network.WLAN(network.STA_IF)
print('network config:', sta_if.ifconfig())
sta_if.active(False)


def do_connect():
    if not sta_if.isconnected():
        print('connecting to network...')
        file = open('1.txt', 'r')
        for line in file:
            sta_if.active(True)
            line = line.split('\n')[0]
            sta_if.connect('Intellect', str(line))
            ftime = time.time()
            now = 0
            while not sta_if.isconnected() and now < 5:
                now = int(time.time() - ftime)
                pass
            print(line, 'is not password!')
            if sta_if.isconnected():
                print('Password found!', line)
                break
            sta_if.active(False)
    else:
        print('Connecting yet!')
    print('network config:', sta_if.ifconfig())

do_connect()
sta_if.active(False)

