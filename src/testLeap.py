import sys
sys.path.insert(0, "../lib")
import Leap


class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        if len(frame.hands) > 0:
            hand = frame.hands[0]
            # print ("There's a hand!")
            if hand.is_right:
                print "\tright hand!", "center:", hand.stabilized_palm_position
            elif hand.is_left:
                print "\tleft hand!", "center:", hand.stabilized_palm_position
        # print "Frame available"


def main():
    # Create a sample listener and controller

    listener = SampleListener()
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
