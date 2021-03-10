import arcade
import math
import os
import time

brick_filedir = "images/brick.png"
box_filedir = "images/box.png"
goal_filedir = "images/goal.png"
player_filedir = "images/player.png"

SPRITE_SCALING = 0.15
METRICS_WIDTH = 400


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BEIGE)

    def setup(self, walls, boxes, goals, player, metrics):
        # Set up your game here
        self.brick_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.boardPopulator(brick_filedir, self.brick_list, walls)
        self.boardPopulator(box_filedir, self.box_list, boxes)
        self.boardPopulator(goal_filedir, self.goal_list, goals)
        self.boardPopulator(player_filedir, self.player_list, [player])
               
        self.metrics = metrics

    def boardPopulator(self, filedir, sprite_list, positions):
        asset = arcade.Sprite(filedir, SPRITE_SCALING)
        x = asset.width/2
        y = asset.height/2

        max_asset_x = int(self.width/asset.width)
        max_asset_y = int(self.height/asset.height)

        for i in range(max_asset_x):
            for j in range(max_asset_y):
                if((i, j) in positions):
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
        # Draw Board
        self.brick_list.draw()
        self.box_list.draw()
        self.goal_list.draw()
        self.player_list.draw()
        
        # Draw metrics
        start_x = self.width - METRICS_WIDTH/2
        start_y = self.height/2
        
        arcade.draw_rectangle_filled(start_x, start_y, METRICS_WIDTH , self.height, arcade.color.BABY_PINK) 
        
        arcade.draw_text("SOKOBAN SOLVER", start_x - 100, start_y + 200, arcade.color.BLACK, 20, anchor_y="top")
        arcade.draw_text("Search Method: " + self.metrics.params, start_x - 120, start_y + 160, arcade.color.BLACK, 18, anchor_y="top")
        if(self.metrics.success == False):
            arcade.draw_text("No Solution", start_x - 90, start_y + 120, arcade.color.BLACK, 16, anchor_y="top")
        else:
            arcade.draw_text("Solution Found", start_x - 90, start_y + 120, arcade.color.BLACK, 16, anchor_y="top")
             
        arcade.draw_text("Depth: %d" %self.metrics.depth, start_x - 140, start_y + 80, arcade.color.BLACK, 15, anchor_y="top")
        arcade.draw_text("Nodes Expanded: %d" %self.metrics.nodes_expanded, start_x - 140, start_y + 55, arcade.color.BLACK, 15, anchor_y="top")
        arcade.draw_text("Nodes in Frontier: %d" %self.metrics.frontier, start_x - 140, start_y + 35, arcade.color.BLACK, 15, anchor_y="top")
        arcade.draw_text("Cost: %d" %self.metrics.cost, start_x - 140, start_y + 15, arcade.color.BLACK, 15, anchor_y="top")
        
        # End
        arcade.finish_render()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def render(min, max, walls, boxes, goals, player, steps, metrics):
    brick = arcade.Sprite(brick_filedir, SPRITE_SCALING)

    SCREEN_WIDTH = (max[0]-min[0]+1)*math.ceil(brick.width) + METRICS_WIDTH
    SCREEN_HEIGHT = (max[1]-min[1]+1)*math.ceil(brick.height) 

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup(walls, boxes, goals, player, metrics)
    
    count = 0
    img_file = "./solutions/%s.png"

    if not os.path.exists('solutions'):
        os.makedirs('solutions')

    game.on_draw()
    # img = arcade.get_image()
    # img.save(img_file % count, 'PNG')

    # player_asset = game.player_list[0]

    for step in steps:
        move_player(game,step)
        count += 1
        time.sleep(0.40)
        game.on_draw()

    arcade.run()

def move_player(game, step):
    player_asset = game.player_list[0]
    if(step == 'l'):
        player_asset.center_x -= player_asset.width
    elif(step == 'r'):
        player_asset.center_x += player_asset.width
    elif(step == 'u'):
        player_asset.center_y += player_asset.height
    else:
        player_asset.center_y -= player_asset.height

    closest_box = arcade.get_closest_sprite(player_asset, game.box_list)

    if(closest_box[1] < 0.1):
        if(step == 'l'):
            closest_box[0].center_x -= closest_box[0].width
        elif(step == 'r'):
            closest_box[0].center_x += closest_box[0].width
        elif(step == 'u'):
            closest_box[0].center_y += closest_box[0].height
        else:
            closest_box[0].center_y -= closest_box[0].height

 
   