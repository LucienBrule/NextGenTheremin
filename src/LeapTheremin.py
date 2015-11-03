"""
@Author:    Lucien Brule <brulel@rpi.edu>
@Credit:    Various online sources
@Descr:     Implements dispatches events for the leap motion to
            function as a Theremin.

"""

import SynthSound
import math
from numpy import interp
import sys
sys.path.append("../lib")
import Leap


def distance(xyz):
    return math.sqrt(xyz[0]**2 + xyz[1]**2 + xyz[2]**2)


class ThereminListener(Leap.Listener):
    lefthandpos = (0, 0, 0)
    righthandpos = (0, 0, 0)

    def __init__(self):
        super(ThereminListener, self).__init__()
        self.sound = SynthSound.Synth()

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        hand = frame.hands[0]
        if len(frame.hands) > 0:
            if hand.is_right:
                # print "\tright hand!", "center:", hand.stabilized_palm_position
                self.righthandpos = hand.stabilized_palm_position
                self.sound.set_frequency(interp(distance(hand.stabilized_palm_position), [0, 300], [250, 550]))
                self.sound.play_tone()
                self.righthandpos = hand.stabilized_palm_position
            elif hand.is_left:
                # print "\tleft hand!", "center:", hand.stabilized_palm_position
                self.sound.set_volume(interp(distance(hand.stabilized_palm_position), [0, 50], [0, 1]))
                self.sound.play_tone()
                self.lefthandpos = hand.stabilized_palm_position

    def get_left_hand_pos(self):
        return {'x': self.lefthandpos[0], 'y': self.lefthandpos[1], 'z': self.lefthandpos[2]}

    def get_right_hand_pos(self):
        return {'x': self.righthandpos[0], 'y': self.righthandpos[1], 'z': self.righthandpos[2]}

    def get_left_hand_rt(self):
        try:
            return (distance(self.lefthandpos), math.atan(self.lefthandpos[0] / self.lefthandpos[1]))
        except ZeroDivisionError:
            print ("I'm affraid I can't let you do that")
            return (distance(self.lefthandpos), math.atan(self.lefthandpos[0] / self.lefthandpos[1] + 1))

    def get_right_hand_rt(self):
        try:
            return (distance(self.righthandpos), math.atan(self.righthandpos[0] / self.righthandpos[1]))
        except ZeroDivisionError:
            print ("I'm affraid I can't let you do that")


def main():
    listener = ThereminListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Do pyaudio stuff

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
