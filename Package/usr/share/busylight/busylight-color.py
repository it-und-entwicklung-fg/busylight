#!/usr/bin/python3

import os, sys, getopt
from configparser import ConfigParser

config_file = "/var/local/busylight/state"
config = ConfigParser()

def main(argv):
    red = green = blue = 0
    try:
        opts, args = getopt.getopt(argv,"hr:g:b:",["red=","green=","blue="])
    except getopt.GetoptError:
        print('busylight-color -r <red> -g <green> -b <blue>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('busylight-color -r <red> -g <green> -b <blue>')
            sys.exit()
        elif opt in ("-r", "--red"):
            red = arg
        elif opt in ("-g", "--green"):
            green = arg
        elif opt in ("-b", "--blue"):
            blue = arg
    print('Red: ', red)
    print('Green: ', green)
    print('Blue: ', blue)
    if os.path.isfile(config_file):
        config.read(config_file)
        rgb = config["RGB"]
        rgb["red"] = str(red)
        rgb["green"] = str(green)
        rgb["blue"] = str(blue)
        with open(config_file, "w+") as conf:
            config.write(conf)
    else:
        print("Service not running")
        print("The background servive that is needed is not running")

if __name__ == "__main__":
   main(sys.argv[1:])