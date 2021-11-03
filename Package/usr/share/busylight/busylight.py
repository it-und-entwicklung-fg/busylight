# Python script for the Python Demo Service

from configparser import ConfigParser
import os.path

if __name__ == '__main__':
    import time
    #from bl import BusyLight
    import systemd.daemon

    # Tell systemd that our service is ready
    systemd.daemon.notify('READY=1')

    config_file = "/var/cache/busylight/config.conf"
    config = ConfigParser()
    config = {
    "red": "0",
    "green": "0",
    "blue": "0"
    }

    while True:
        if os.path.isfile(config_file):
            config.read(config_file)
            rgb = config["RGB"]
            if len(rgb) >= 3:
                print("Red: " + rgb["red"])
                print("Green: " + rgb["green"])
                print("Blue: " + rgb["blue"])
                #BusyLight(int(rgb[0]),int(rgb[1]),int(rgb[2]))
        else:
            #Write the above sections to config.ini file
            with open(config_file, 'w') as conf:
                config.write(conf)
        time.sleep(2)

