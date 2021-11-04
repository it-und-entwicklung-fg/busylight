#!/usr/bin/env python3
import hid


class BusyLight(object):
    """
    Simple class for BusyLight
    """

    def __init__(self, red=0, green=0, blue=0, blink=0, vendor_id=0x27bb, product_id=0x3bcd):
        self.red = red
        self.green = green
        self.blue = blue
        self.blink_rate = blink

        self._vendor_id = vendor_id
        self._product_id = product_id
        self.buffer = None

        self.positions = {
            'r': 3,
            'g': 4,
            'b': 5,
            't': 8,
            'blink': 7,
        }

        self.device = hid.device()
        self.device.open(self._vendor_id, self._product_id)
        self.device.set_nonblocking(1)

        self.reset_buffer()
        self.update_buffer()
        self.write()
        self.device.close()

    def reset_buffer(self):
        """
        Method to reset the buffer to remove light/sound. 
        """
        # 0 = time
        # 1 = next step
        # 2 = repeat
        # 3 = red
        # 4 = green
        # 5 = blue
        # 6 = on Time
        # 7 = off Time
        # 8 = ringtone

        self.buffer = [0, 16, 0, 0, 0, 0, 0, 0, 128] \
                      + [0] * 50 \
                      + [255, 255, 255, 255, 6, 147]
        self.write()

    def update_buffer(self):
        """
        Method to update the buffer.
        """

        # update the colors and blink rate
        self.buffer[self.positions['r']] = self.red
        self.buffer[self.positions['g']] = self.green
        self.buffer[self.positions['b']] = self.blue
        self.buffer[self.positions['blink']] = 0

        # update the checksum
        checksum = sum(self.buffer[0:63])
        self.buffer[63] = (checksum >> 8) & 0xffff
        self.buffer[64] = checksum % 256

    def set_color(self, r, g, b, blink_rate=0):
        # Set the color
        self.red = r
        self.green = g
        self.blue = b
        self.blink_rate = blink_rate

    def write(self, buff=None):
        """
        Method to write buffer to BusyLight
        """

        if buff is not None:
            self.buffer = buff
        self.device.write(self.buffer)

    def close(self):
        self.device.close()


def is_plugged_in(vendor_id=0x27bb, product_id=0x3bcd):
    return len(hid.enumerate(vendor_id, product_id)) > 0
