#!/usr/bin/env python3
import time
import hid

class BusyLight(object):
    """
    Simple class for BusyLight
    """
    def __init__(self, red=0, green=0, blue=0, blink=0, tone='quiet', vol=0,
                 vendor_id=0x27bb, product_id=0x3bcd):
        
        self.tone_names = [
            'openoffice',
            'funky',
            'fairytale',
            'kuandotrain',
            'telephonenordic',
            'telephoneoriginal',
            'telephonepickmeup',
            'buzz'
        ]

        self.red=red
        self.green=green
        self.blue=blue
        self.blink_rate=blink
        if hasattr(tone, 'capitalize'):
            self.tone=tone
        else:
            self.tone=self.tone_names[tone]
        self.vol=vol
        self._vendor_id = vendor_id
        self._product_id = product_id
        self.buffer = None

        self.positions = {
            'r': 3,
            'g': 4,
            'b': 5,
            't': 8,
            'blink':7,
        }
        
        self.tones = {
            'openoffice'        : 136,
            'quiet'             : 144,
            'funky'             : 152,
            'fairytale'         : 160,
            'kuandotrain'       : 168,
            'telephonenordic'   : 176,
            'telephoneoriginal' : 184,
            'telephonepickmeup' : 192,
            'buzz'              : 216,
        }

        self.device = hid.device()
        self.device.open(self._vendor_id, self._product_id)
        self.device.set_nonblocking(1)

        self.reset_buffer()
        self.update_buffer()
        self.write()

    def reset_buffer(self):
        """
        Method to reset the buffer to remove light/sound. 
        """
        # 0 = time
        # 1 = next step
        # 2 = Repeat
        # 3 = Rot
        # 4 = Grün
        # 5 = Blau
        # 6 = on Time
        # 7 = off Time
        # 8 = Klingelton
        
        self.buffer = [0,16,0,0,0,0,0,0,128] \
                      + [0]*50 \
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
        # update the tone 
        self.buffer[self.positions['t']] = self.tones[self.tone]
        # ubdate volume
        self.buffer[self.positions['t']] += self.vol

        # update the checksum
        checksum = sum(self.buffer[0:63])
        self.buffer[63] = (checksum >> 8) & 0xffff
        self.buffer[64] = checksum % 256

    def set_color(self,r,g,b, blink_rate=0):
        #Set the color
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

def clear_bl():
    """
    Function to clear the buffer and display/play nothing.
    """
    bl = BusyLight()
    bl.write()
    bl.close()


def color_setter(red=0, green=0, blue=0, blink=0):
    bl = BusyLight()
    bl.set_color(red, green, blue)
    bl.update_buffer()
    bl.write()
    bl.close()
