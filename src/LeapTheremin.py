"""
@Author:    Lucien Brule <brulel@rpi.edu>
@Credit:    Various online sources
@Descr:     Implements dispatches events for the leap motion to
            function as a Theremin.

"""
import sys
sys.path.insert(0, "../lib")
import Leap
import SynthSound
from numpy import interp



class ThereminListener(Leap.Listener):

    def __init__(self):
        super(ThereminListener, self).__init__()
        self.sound = SynthSound.Synth()

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        if len(frame.hands) > 0:
            hand = frame.hands[0]
            if hand.is_right:
                print "\tright hand!", "center:", hand.stabilized_palm_position
                self.sound.set_frequency(interp(abs(hand.stabilized_palm_position[0]),[0,300],[250,550]))
            elif hand.is_left:
                print "\tleft hand!", "center:", hand.stabilized_palm_position
                self.sound.set_volume(interp(abs(hand.stabilized_palm_position[0]),[300,0],[0,1]))
        self.sound.play_tone()

def main():
    # Create a sample listener and controller

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
