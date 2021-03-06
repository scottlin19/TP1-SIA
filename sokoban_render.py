import arcade
import math

brick_filedir = "images/brick.png"
box_filedir = "images/box.png"
goal_filedir = "images/goal.png"
player_filedir = "images/player.png"

SPRITE_SCALING = 0.15


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BEIGE)

    def setup(self, walls, boxes, goals, player):
        # Set up your game here
        self.asset_list = arcade.SpriteList()
        print(player)

        self.boardPopulator(brick_filedir, walls)
        self.boardPopulator(box_filedir, boxes)
        self.boardPopulator(goal_filedir, goals)
        self.boardPopulator(player_filedir, player)

    def boardPopulator(self, filedir, positions):
        asset = arcade.Sprite(filedir, SPRITE_SCALING)
        x = asset.width/2
        y = asset.height/2

        max_asset_x = int(self.width/asset.width)
        max_asset_y = int(self.height/asset.height)

        for i in range(max_asset_x):
            for j in range(max_asset_y):
                if([i, j] in positions):
                    asset.center_x = x
                    asset.center_y = y
                    self.asset_list.append(asset)
                    asset = arcade.Sprite(filedir, SPRITE_SCALING)

                y += asset.height

            x += asset.width
            y = asset.height/2

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.asset_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def render(min, max, walls, boxes, goals, player):
    brick = arcade.Sprite(brick_filedir, SPRITE_SCALING)

    SCREEN_WIDTH = (max[0]-min[0]+1)*math.ceil(brick.width)
    SCREEN_HEIGHT = (max[1]-min[1]+1)*math.ceil(brick.height)

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup(walls, boxes, goals, player)
    arcade.run()


# if __name__ == "__main__":
#     main()