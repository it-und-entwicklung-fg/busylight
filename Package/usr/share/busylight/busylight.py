# Python script for the Python Demo Service

from configparser import ConfigParser
import os.path

from bl import is_plugged_in

if __name__ == '__main__':
    import time
    from bl import BusyLight
    import systemd.daemon

    # Tell systemd that our service is ready
    systemd.daemon.notify('READY=1')

    config_file = "/var/cache/busylight/config.conf"
    config = ConfigParser()
    config["RGB"] = {
        "red": "0",
        "green": "0",
        "blue": "0"
    }

    while True:
        if is_plugged_in():
            if os.path.isfile(config_file):
                config.read(config_file)
                rgb = config["RGB"]
                if len(rgb) >= 3:
                    red = int(rgb["red"])
                    green = int(rgb["green"])
                    blue = int(rgb["blue"])
                    if (0 <= red <= 255) and (0 <= green <= 255) and (0 <= blue <= 255):
                        BusyLight(red, green, blue)
                    else:
                        print("RGB value to small or to large!")
            else:
                # Write the above sections to config.ini file
                with open(config_file, 'w') as conf:
                    config.write(conf)
        else:
            print("Device not found!")
        time.sleep(0.1)
