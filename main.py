from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
class PongBall(Widget):
    velocity_x = NumericProperty(5)
    velocity_y = NumericProperty(5)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    def move(self):
        self.pos = Vector(self.velocity) + self.pos
class PongGame(Widget):
    ball = ObjectProperty(None)
    def update(self, dt):
        self.ball.move()
        if self.ball.x < self.x:
            self.ball.velocity_x *= -1
        elif self.ball.right > self.width:
            self.ball.velocity_x *= -1
        elif self.ball.y < self.y:
            self.ball.velocity_y *= -1
        elif self.ball.top > self.height:
            self.ball.velocity_y *= -1
class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1/60)
        return game
app = PongApp()
app.run()