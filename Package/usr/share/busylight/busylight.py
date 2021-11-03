# Python script for the Python Demo Service

if __name__ == '__main__':
    import time
    from bl import BusyLight
    import systemd.daemon

    # Tell systemd that our service is ready
    systemd.daemon.notify('READY=1')

    while True:
        rgbfile = open("/var/cache/busylight/rgb", "r")
        rgb=rgbfile.readlines()
        if len(rgb) >= 3:
            print("Red: " + rgb[0])
            print("Green: " + rgb[1])
            print("Blue: " + rgb[2])
            #BusyLight(int(rgb[0]),int(rgb[1]),int(rgb[2]))
        rgbfile.close()
        time.sleep(2)

