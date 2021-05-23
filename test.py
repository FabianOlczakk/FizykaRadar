from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
<RotatingLineWidget>:
    canvas:
        PushMatrix
        Translate:
            xy: self.pos[0], self.pos[1]
        Rotate:
            angle: -self.angle
            origin: self.bottom
        Color:
            rgba: 1, 1, 1, 1
        Line:
            points: 0, -self.length * 0.5, 0, self.length * 0.5
            width: 2
        PopMatrix
''')


class RotatingLineWidget(Widget):
    length = NumericProperty(10.0)
    angle = NumericProperty()

    def __init__(self, **kwargs):
        super(RotatingLineWidget, self).__init__(**kwargs)

if __name__ == "__main__":
    from kivy.base import runTouchApp
    from kivy.uix.floatlayout import FloatLayout
    from kivy.animation import Animation
    from kivy.properties import ObjectProperty
    from kivy.clock import Clock

    Builder.load_string('''
<MainWindow>:
    line: line
    RotatingLineWidget:
        id: line
        length: 200
        angle: 0
        pos: root.size[0]/2, root.size[1]/2
''')

    class MainWindow(FloatLayout):
        line = ObjectProperty()

        def __init__(self, **kwargs):
            super(MainWindow, self).__init__(**kwargs)
            Clock.schedule_interval(self.animate, 2)

        def animate(self, *largs):
            self.line.angle = 0
            a = Animation(angle=180, t='in_out_quad')
            a.start(self.line)

    float_layout = MainWindow()
    runTouchApp(float_layout)