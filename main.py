from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
import pygame
import math


class RadarDot(Widget):
    def on_line(self, x1, y1, x2, y2):
        Q = pygame.math.Vector2(self.x, self.y)
        r = self.width
        P1 = pygame.math.Vector2(x1, y1)
        V = pygame.math.Vector2(x2, y2) - P1

        a = V.dot(V)
        b = 2 * V.dot(P1 - Q)
        c = P1.dot(P1) + Q.dot(Q) - 2 * P1.dot(Q) - r**2

        disc = b**2 - 4 * a * c
        if disc < 0:
            return False, None

        sqrt_disc = math.sqrt(disc)
        t1 = (-b + sqrt_disc) / (2 * a)
        t2 = (-b - sqrt_disc) / (2 * a)

        if not (0 <= t1 <= 1 or 0 <= t2 <= 1):
            return False, None

        t = max(0, min(1, - b / (2 * a)))
        return True, P1 + t * V


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

    def animate(self, *largs):
        """Funkcja animacji wskazówki radaru"""
        a = Animation(angle=self.current_angle, t='in_out_sine', duration=0.5)
        a.start(self)

    def on_current_angle(self, *args):
        """Funkcja wykonywana po zmianie kątu wskazówki"""
        Clock.schedule_once(self.animate, 0)


class RadarApp(MDApp):
    """Głowna klasa aplikacji"""

    def build(self):
        # Tworzę niezbędne połączenia między obiektami
        self.line = self.root.ids.line

    def on_start(self):
        pass


if __name__ == '__main__':
    RadarApp().run()

