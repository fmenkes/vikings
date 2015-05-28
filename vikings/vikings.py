import pyglet
from game import resources, player, board

# change this if you change the tile size!
TILE_SIZE = 16

game_window = pyglet.window.Window(1200, 800)
main_batch = pyglet.graphics.Batch()
game_board = board.random_board(window=game_window, tile_size=TILE_SIZE, batch=main_batch)
player_ship = player.Player(window=game_window, game_board=game_board, tile_size=TILE_SIZE, batch=main_batch)
game_objects = [game_board, player_ship]

for handler in player_ship.event_handlers:
    game_window.push_handlers(handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()

if __name__ == '__main__':
   pyglet.app.run()