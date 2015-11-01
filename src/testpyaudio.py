import math
import pyaudio


def playtone():
    PyAudio = pyaudio.PyAudio
    BITRATE = 16000  # number of frames per second/frameset.
    # See http://www.phy.mtu.edu/~suits/notefreqs.html
    FREQUENCY = 261.63  # Hz, waves per second, 261.63=C4-note.
    LENGTH = 1  # seconds to play sound

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''
    for x in xrange(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))
    # # fill remainder of frameset with silence
    # for x in xrange(RESTFRAMES):
    #     WAVEDATA = WAVEDATA + chr(128)
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)
    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()


def main():
    while True:
        playtone()
        # time.sleep(.01)
if __name__ == "__main__":
    main()
