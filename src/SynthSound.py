"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import time
import math


class SynthSound:

    def __init__(self):
        # default consts
        self.DEFAULTBASE = .001
        self.DEFAULTVOLUME = 10
        self.DEFAULTBITRATE = 16000
        self.DEFAULTPITCHSHIFT = .001
        # variable variables
        self.BASE = self.DEFAULTBASE
        self.BITRATE = self.DEFAULTBITRATE
        self.VOLUME = self.DEFAULTVOLUME
        self.PITCHSHIFT = self.DEFAULTPITCHSHIFT  # If it's zero, then there's no beat frequency (for debug)

    def init(self):
        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        def callback(in_data, frame_count, time_info, status):
            data = self.get_wave(self.VOLUME, self.PITCHSHIFT)
            return (data, pyaudio.paContinue)

        # open stream using callback (3)
        stream = p.open(format=p.get_format_from_width(1),
                        channels=1,
                        rate=16000,
                        output=True,
                        stream_callback=callback)

        # start the stream (4)
        stream.start_stream()

        # wait for stream to finish (5)
        while stream.is_active():
            time.sleep(self.BASE)

        # stop stream (6)
        stream.stop_stream()
        stream.close()

        # close PyAudio (7)
        p.terminate()

    def get_wave(self, volume, pitchshift):

        length = self.BASE + self.PITCHSHIFT
        numberofframes = int(self.BITRATE * length)
        trailingframes = numberofframes % self.BITRATE
        WAVEDATA = ''
        for y in range(0, 50):
            for x in xrange(numberofframes):
                WAVEDATA = WAVEDATA + \
                    chr(int(math.sin(x / ((self.BITRATE / self.VOLUME + y) / math.pi)) * 127 + 128))
            # fill remainder of frameset with silence
        for x in xrange(trailingframes):
            WAVEDATA = WAVEDATA + chr(128)
        return WAVEDATA

    def set_BASE(self, val):
        self.BASE = val

    def set_BITRATE(self, val):
        self.BITRATE = val

    def set_VOLUME(self, val):
        self.VOLUME = val

    def set_PITCHSHIFT(self, val):
        self.PITCHSHIFT = val

    def incr_PICHSHIFT(self, val):
        self.PITCHSHIFT += val


def main():
    mysound = SynthSound()
    mysound.init()

if __name__ == "__main__":
    main()
