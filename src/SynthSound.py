"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import time
import math
import threading
import struct
import time


class Synth:

    # default consts
    DEFAULTBASE = .001
    DEFAULTVOLUME = .5
    DEFAULTBITRATE = 16000
    DEFAULTFREQUENCY = 195
    DURATION = .01

    def __init__(self, interval=1):
        # # threading
        # self.interval = interval
        # thread = threading.Thread(target=self.run, args=())
        # thread.daemon = True                            # Daemonize thread
        # thread.start()                                  # Start the execution

        # variable variables
        self.BASE = self.DEFAULTBASE
        self.BITRATE = self.DEFAULTBITRATE
        self.VOLUME = self.DEFAULTVOLUME
        self.FREQUENCY = 195
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=self.BITRATE,
                             output=True)
    def stop(self):
        # stop stream (6)
        self.stream.stop_stream()
        self.stream.close()

        # close PyAudio (7)
        self.p.terminate()

    def play_tone(self):
        N = int(self.BITRATE / self.FREQUENCY)
        T = int(self.FREQUENCY * self.DURATION)  # repeat for T cycles
        dt = 1.0 / self.BITRATE
        # 1 cycle
        tone = (self.VOLUME * math.sin(2 * math.pi * self.FREQUENCY * n * dt)
                for n in xrange(N))
        # todo: get the format from the stream; this assumes Float32
        data = ''.join(struct.pack('f', samp) for samp in tone)
        for n in xrange(T):
            self.stream.write(data)

    def set_BASE(self, val):
        self.BASE = val

    def set_BITRATE(self, val):
        self.BITRATE = val

    def set_VOLUME(self, val):
        self.VOLUME = val

    def set_FREQUENCY(self, val):
        self.FREQUENCY = val


def main():
    mysound = Synth()

    for x in range(0,100):
        mysound.play_tone()
        mysound.set_FREQUENCY(mysound.FREQUENCY + x)

if __name__ == "__main__":
    main()
