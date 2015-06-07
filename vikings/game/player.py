import pyglet
from pyglet.window import key
import resources
import tile
import random


class Player(pyglet.sprite.Sprite):
    """Class that playable objects (units and ships) inherit from."""
    
    def __init__(self, window, tile_size, game_board, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self.tile_size = tile_size
        self.game_board = game_board
        self.window = window
        self.max_height = self.window.height - self.tile_size
        self.max_width = self.window.width - self.tile_size
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.new_objects = []
        self.check_for_removal = False
        self.can_traverse_water = False
        self.can_be_transported = False
        self.saved_position = ()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.H or symbol == key.LEFT:
            if self.x > 0:
                self.x -= self.tile_size
                if not self.check_position(self.x, self.y):
                    self.x += self.tile_size
        elif symbol == key.L or symbol == key.RIGHT:
            if self.x < self.max_width:
                self.x += self.tile_size
                if not self.check_position(self.x, self.y):
                    self.x -= self.tile_size
        elif symbol == key.J or symbol == key.DOWN:
            if self.y > 0:
                self.y -= self.tile_size
                if not self.check_position(self.x, self.y):
                    self.y += self.tile_size
        elif symbol == key.K or symbol == key.UP:
            if self.y < self.max_height:
                self.y += self.tile_size
                if not self.check_position(self.x, self.y):
                    self.y -= self.tile_size
        elif symbol == key.Y:
            if self.y < self.max_height and self.x > 0:
                self.y += self.tile_size
                self.x -= self.tile_size
                if not self.check_position(self.x, self.y):
                    self.y -= self.tile_size
                    self.x += self.tile_size
        elif symbol == key.U:
            if self.y < self.max_height and self.x < self.max_width:
                self.y += self.tile_size
                self.x += self.tile_size
                if not self.check_position(self.x, self.y):
                    self.y -= self.tile_size
                    self.x -= self.tile_size
        elif symbol == key.B:
            if self.y > 0 and self.x > 0:
                self.y -= self.tile_size
                self.x -= self.tile_size
                if not self.check_position(self.x, self.y):
                    self.y += self.tile_size
                    self.x += self.tile_size
        elif symbol == key.N:
            if self.y > 0 and self.x < self.max_width:
                self.y -= self.tile_size
                self.x += self.tile_size
                if not self.check_position(self.x, self.y):
                    self.y += self.tile_size
                    self.x -= self.tile_size

    def look_up_tile(self, x, y):
        x = x/self.tile_size
        y = y/self.tile_size

        return self.game_board[((self.window.height/self.tile_size)*x+y)]

    def check_position(self, x, y):
        if self.can_traverse_water:
            if type(self.look_up_tile(x, y)) is not tile.WaterTile:
                player_unit = PlayerUnit(window=self.window, game_board=self.game_board, tile_size=self.tile_size,
                                         x=self.x, y=self.y, batch=self.batch)
                self.new_objects.append(player_unit)
                return False
        elif type(self.look_up_tile(x, y)) is tile.WaterTile:
            if self.can_be_transported:
                self.saved_position = (x, y)
                self.check_for_removal = True
            return False

        return True

class PlayerUnit(Player):
    def __init__(self, *args, **kwargs):
        super(PlayerUnit, self).__init__(img=resources.unit_tile, *args, **kwargs)

        self.can_be_transported = True


class PlayerShip(Player):
    def __init__(self, *args, **kwargs):
        super(PlayerShip, self).__init__(img=resources.ship_tile, *args, **kwargs)

        self.can_traverse_water = True

        while True:
            random_tile = self.game_board[random.randrange(0, len(self.game_board))]
            if type(random_tile) is tile.WaterTile:
                self.x = random_tile.x
                self.y = random_tile.y
                break
