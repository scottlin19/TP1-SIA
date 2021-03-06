import arcade
import math
import os


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
        self.brick_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.boardPopulator(brick_filedir, self.brick_list, walls)
        self.boardPopulator(box_filedir, self.box_list, boxes)
        self.boardPopulator(goal_filedir, self.goal_list, goals)
        self.boardPopulator(player_filedir, self.player_list, [player])

    def boardPopulator(self, filedir, sprite_list, positions):
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
                    sprite_list.append(asset)
                    asset = arcade.Sprite(filedir, SPRITE_SCALING)

                y += asset.height

            x += asset.width
            y = asset.height/2

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.brick_list.draw()
        self.box_list.draw()
        self.goal_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def render(min, max, walls, boxes, goals, player, steps):
    brick = arcade.Sprite(brick_filedir, SPRITE_SCALING)

    SCREEN_WIDTH = (max[0]-min[0]+1)*math.ceil(brick.width)
    SCREEN_HEIGHT = (max[1]-min[1]+1)*math.ceil(brick.height)

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup(walls, boxes, goals, player)

    count = 0
    img_file = "./solutions/%s.png"

    if not os.path.exists('solutions'):
        os.makedirs('solutions')

    game.on_draw()
    img = arcade.get_image()
    img.save(img_file % count, 'PNG')

    player_asset = game.player_list[0]

    for step in steps:
        if(step == 'l'):
            player_asset.center_x -= player_asset.width
        elif(step == 'r'):
            player_asset.center_x += player_asset.width
        elif(step == 'u'):
            player_asset.center_y += player_asset.height
        else:
            player_asset.center_y -= player_asset.height
        count += 1
        game.on_draw()
        img = arcade.get_image()
        img.save(img_file % count, 'PNG')

    # arcade.run()


# if __name__ == "__main__":
#     main()