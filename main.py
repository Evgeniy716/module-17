import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGT = 600
SCREEN_TITLE = "Pong Game"

class Ball(arcade.Window):


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("bar.png",0.1)

class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.bar = Bar()
        self.setup()



    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGT / 5



if __name__ == "__main__":
    window = Game(SCREEN_WIDTH,SCREEN_HEIGT,SCREEN_TITLE)
    arcade.run()
