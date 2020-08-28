# step1:create app
# 2:create the game
# 3:build the game
# 4:run the app

from kivy.app import App
from kivy.uix.widget import Widget #widget is like blank canvas


class PongGame(Widget):
    pass
class PongApp(App):
    def build(self):
        return PongGame()

PongApp().run()