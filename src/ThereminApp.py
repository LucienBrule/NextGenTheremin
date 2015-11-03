#!/usr/bin/kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.widget import NumericProperty
from kivy.uix.widget import ObjectProperty
from kivy.clock import Clock
import LeapTheremin


# It's a circle that moves
class Hand(Widget):
    pos = NumericProperty(0)

    def update_position(self, pos):
        self.x = pos.x
        self.y = pos.y


class Instrument(Widget):
    pos = NumericProperty(0)


class ThereminVis(Widget):
    leaptheremin = LeapTheremin.ThereminListener()
    lefthand = ObjectProperty(None)
    righthand = ObjectProperty(None)
    instrument = ObjectProperty(None)

    def update(self, dt):
        self.lefthand.update_position()
        self.righthand.update_position()


class ThereminApp(App):

    def build(self):
        vis = ThereminVis()
        Clock.schedule_interval(vis.update, 1.0 / 60.0)
        return vis

if __name__ == '__main__':
    ThereminApp().run()
