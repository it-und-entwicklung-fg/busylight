#!/usr/bin/python3

from configparser import ConfigParser
from contextlib import nullcontext
import os.path
import time
import systemd.daemon
from bl import BusyLight
from bl import is_plugged_in

def create_state_cfg(state_file):
    # Write the above sections to config.ini file
    with open(state_file, 'w') as sf:
        state_cfg.add_section('current')
        state_cfg.set('current', 'state', 'UNAVAILABLE')
        state_cfg.write(sf)

if __name__ == '__main__':
    # Tell systemd that our service is ready
    systemd.daemon.notify('READY=1')

    state_file = "/var/local/busylight/state"
    state_cfg = ConfigParser()

    definition_file = "/etc/busylight/definitions.conf"
    definition_cfg = ConfigParser()

    red_old = 0
    green_old = 0
    blue_old = 0

    global t
    t = 0

    while True:
        if is_plugged_in():
            if os.path.isfile(state_file) and os.path.isfile(definition_file):
                state_cfg.read(state_file)
                definition_cfg.read(definition_file)
                current = state_cfg["current"]
                if 'state' in current:
                    state = current["state"]
                    if state in definition_cfg:
                        red = 0
                        green = 0
                        blue = 0
                        blink = 'false'
                        if 'red' in definition_cfg[state]:
                            red = int(definition_cfg.get(state, 'red'))
                        if 'green' in definition_cfg[state]:
                            green = int(definition_cfg.get(state, 'green'))
                        if 'blue' in definition_cfg[state]:
                            blue = int(definition_cfg.get(state, 'blue'))
                        if 'blink' in definition_cfg[state]:
                            if definition_cfg.get(state, 'blink') == 'true':
                                blink = 1
                            else:
                                blink = 0
                                print(definition_cfg.get(state, 'blink'))
                        print('Red:', red, 'Green:', green, 'Blue:', blue, 'Blink:', blink)
                    else:
                        print(state, "not found in definitions file!")
                    if red == red_old and blue == blue_old and green == green_old and blink == 1:
                        print(t)
                        if t == 0 or t == 6:
                            BusyLight(red, green, blue)
                            t = 1
                        elif t == 3:
                            BusyLight(0, 0, 0)
                            t = t + 1
                        else:
                            t = t + 1
                    else:
                        BusyLight(red, green, blue)
                        red_old = red
                        green_old = green
                        blue_old = blue
                else:
                    create_state_cfg(state_file)
                    print("'state' not found")
            else:
                create_state_cfg(state_file)
                print("Config not found")
        else:
            print("Busylight not connected!")
        time.sleep(0.1)
