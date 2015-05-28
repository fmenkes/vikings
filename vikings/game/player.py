import pyglet
from pyglet.window import key
import resources
import tile
import random


class Player(pyglet.sprite.Sprite):
    
    def __init__(self, window, tile_size, game_board, *args, **kwargs):
        super(Player, self).__init__(img=resources.ship_tile, *args, **kwargs)

        self.tile_size = tile_size
        self.game_board = game_board
        self.window = window
        self.max_height = self.window.height - self.tile_size
        self.max_width = self.window.width - self.tile_size
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        while True:
            random_tile = game_board[random.randrange(0, len(game_board))]
            if type(random_tile) is tile.WaterTile:
                self.x = random_tile.x
                self.y = random_tile.y
                break

    def on_key_press(self, symbol, modifiers):
        if symbol == key.H:
            if self.x > 0:
                self.x -= self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.x += self.tile_size
        elif symbol == key.L:
            if self.x < self.max_width:
                self.x += self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.x -= self.tile_size
        elif symbol == key.J:
            if self.y > 0:
                self.y -= self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.y += self.tile_size
        elif symbol == key.K:
            if self.y < self.max_height:
                self.y += self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.y -= self.tile_size
        elif symbol == key.Y:
            if self.y < self.max_height and self.x > 0:
                self.y += self.tile_size
                self.x -= self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.y -= self.tile_size
                    self.x += self.tile_size
        elif symbol == key.U:
            if self.y < self.max_height and self.x < self.max_width:
                self.y += self.tile_size
                self.x += self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.y -= self.tile_size
                    self.x -= self.tile_size
        elif symbol == key.B:
            if self.y > 0 and self.x > 0:
                self.y -= self.tile_size
                self.x -= self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.y += self.tile_size
                    self.x += self.tile_size
        elif symbol == key.N:
            if self.y > 0 and self.x < self.max_width:
                self.y -= self.tile_size
                self.x += self.tile_size
                if type(self.look_up_tile(self.x, self.y)) is not tile.WaterTile:
                    self.y += self.tile_size
                    self.x -= self.tile_size

    def look_up_tile(self, x, y):
        x = x/self.tile_size
        y = y/self.tile_size

        return self.game_board[((self.window.height/self.tile_size)*x+y)]
