from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from api import Radar
import random
import math


class AngleLabel(MDLabel):
    pass


class RadarDot(Widget):
    random_color = [random.random(), random.random(), random.random(), 1]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.auto_destruct, 4)

    def auto_destruct(self, *args):
        self.parent.remove_widget(self)


class RotateButton(Button):
    def callback(self, *args):
        """Funkja wykonywana po wciśnięciu przycisku"""
        self.line.current_angle = int(self.input.text) - 90

        print("Input text: " + str(self.input.text))


class RotationInput(MDTextField):
    pass


class RotatingLineWidget(Widget):
    """Klasa wskazówki"""

    # Tworzę niezbęde zmienne
    length = NumericProperty(10.0)
    angle = NumericProperty()
    current_angle = NumericProperty()
    current_distance = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        try:
            self.myradar = Radar('/dev/tty.usbmodem14202')

        except Exception:
            pass

        Clock.schedule_interval(self.start_radar_update, 0)

    def start_radar_update(self, *args):

        try:
            data = self.myradar.get_data()

            # print(data)

            angle = data['angle']
            distance = int(data['distance'])

            angle = int(angle)

            angle = angle - 90

            self.current_angle = angle
            self.current_distance = distance

        except Exception:
            self.current_angle = 34

    def animate(self, *largs):
        """Funkcja animacji wskazówki radaru"""
        a = Animation(angle=self.current_angle, t='in_out_sine', duration=0)
        a.start(self)

    def add_dot(self):
        dot_distance = self.myradar.get_data()
        dot_angle = self.myradar.get_data()

        dot_angle = dot_angle['angle']
        dot_distance = dot_distance['distance']

        dot_distance = dot_distance * 2

        # print(dot_angle)

        if dot_distance != 0:
            x = dot_distance * math.cos(math.radians(dot_angle))
            print(x)
            y = dot_distance * math.sin(math.radians(dot_angle))
            print(y)

            # print(str(x), str(y))
            self.main_float.add_widget(RadarDot(pos=(x, y)))

        # print(dot_angle)

    def angle_change(self, *args):
        self.animate()

    def distance_change(self, *args):
        self.add_dot()

    def on_current_distance(self, *args):
        Clock.schedule_once(self.distance_change, 0)

    def on_current_angle(self, *args):
        """Funkcja wykonywana po zmianie kątu wskazówki"""
        Clock.schedule_once(self.angle_change, 0)


class RadarApp(MDApp):
    """Głowna klasa aplikacji"""

    def build(self):
        # Tworzę niezbędne połączenia między obiektami
        self.line = self.root.ids.line

    def on_start(self):
        pass


if __name__ == '__main__':
    RadarApp().run()

