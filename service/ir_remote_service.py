#!/usr/bin/python
# -*- coding: utf-8 -*-

from evdev import UInput, ecodes as e
import serial
import sys
import time
import json

#port = "/dev/ttyUSB1"
baudrate = 115200


def takeSecond(elem):
    return elem['remote']


def main(port):
    codes = []
    previus_key = None
    key_to_send = None
    previus_milli_sec = 0
    current_milli_sec = 0
    remote_to_key_map = {}

    ser = serial.Serial(port, baudrate)

    # Reset arduino
    ser.setDTR(1)
    time.sleep(0.25)
    ser.setDTR(0)

    # Load config
    with open('/etc/ir-arduino-remote/keys.json') as json_file:
        data = json.load(json_file)
        codes = list(filter(lambda x: x['remote'] != '', data['lists']))
        remote_to_key_map = {d['remote']: d['key'] for d in codes}
        print('Loaded: %d codes' % len(codes))
        print(remote_to_key_map)

    # Open Uinput
    ui = UInput()

    # Main loop
    while True:
        remote_input_bytes = ser.readline()
        remote_input_str = remote_input_bytes.decode("utf-8").replace('\n', '')

        # Ignore start and stop input
        if remote_input_str == 'F0610CF3':
            continue

        k = ''
        for ii in codes:
            if ii['remote'] == remote_input_str:
                k = ii['name']
        print('IR: %s:%s' % (remote_input_str, k))

        current_milli_sec = int(round(time.time() * 1000))

        delay = current_milli_sec - previus_milli_sec

        # repeat previus key
        if remote_input_str == 'FFFFFFFF' and previus_key != None:
            print('D: %d' % delay)
            if delay > 100:
                print('rep: %d' % previus_key)
                ui.write(e.EV_KEY, previus_key, 1)
                ui.write(e.EV_KEY, previus_key, 0)
                ui.syn()
            else:
                print('deounce')

        elif key_to_send := remote_to_key_map.get(remote_input_str, None):
            print('key_to_send: %d' % key_to_send)
            ui.write(e.EV_KEY, key_to_send, 1)
            ui.write(e.EV_KEY, key_to_send, 0)
            ui.syn()
            previus_key = key_to_send
            previus_milli_sec = int(round(time.time() * 1000))
        else:
            previus_key = None


if __name__ == "__main__":
    port = "/dev/ttyUSB0"

    if len(sys.argv) > 1:
        port = sys.argv[1]

    main(port)
