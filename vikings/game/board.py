import pyglet
import numpy
import tile
import worldgen


def init_board(window, tile_size, batch):
    """Create a game board, using window as a parameter.

    The window x and y must be divisible by tile_size"""

    game_board = []

    for y in xrange(0, window.height/tile_size):
        game_board.append([tile.WaterTile(x=x*tile_size, y=y*tile_size, batch=batch) for x in xrange(0, window.width/tile_size)])


    return game_board


def random_board(window, tile_size, batch):

    game_board = []

    generated_board = worldgen.hill_algorithm(window.width, window.height, tile_size)
    
    for coordinate in generated_board:
        if coordinate[2] >= 14:
            game_board.append(tile.MountainTile(x=coordinate[0]*tile_size, y=coordinate[1]*tile_size, batch=batch))
        elif coordinate[2] >= 6:
            game_board.append(tile.GrassTile(x=coordinate[0]*tile_size, y=coordinate[1]*tile_size, batch=batch))
        elif coordinate[2] >= 5:
            game_board.append(tile.SandTile(x=coordinate[0]*tile_size, y=coordinate[1]*tile_size, batch=batch))
        else:
            game_board.append(tile.WaterTile(x=coordinate[0]*tile_size, y=coordinate[1]*tile_size, batch=batch))


    return game_board