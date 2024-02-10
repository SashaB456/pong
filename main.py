from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height/2)
            new_velocity = Vector(-1*vx, offset+vy)
            new_velocity *= 1.1
            ball.velocity = new_velocity
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    def move(self):
        self.pos = Vector(self.velocity) + self.pos
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    def serve_ball(self, vel=Vector(5, 0).rotate(randint(0,360))):
        self.ball.center = self.center
        self.ball.velocity = vel
    def update(self, dt):
        self.ball.move()
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        if self.ball.y < self.y:
            self.ball.velocity_y *= -1
        elif self.ball.top > self.height:
            self.ball.velocity_y *= -1
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(5, 0))
        elif self.ball.right > self.right:
            self.player1.score += 1
            self.serve_ball(vel=(-5, 0))
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        elif touch.x > self.width*2/3:
            self.player2.center_y = touch.y
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1/60)
        return game
app = PongApp()
app.run()