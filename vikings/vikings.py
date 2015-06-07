import pyglet
from game import resources, player, board

# change this if you change the tile size!
TILE_SIZE = 16

game_window = pyglet.window.Window(1200, 800)
main_batch = pyglet.graphics.Batch()
game_board = board.random_board(window=game_window, tile_size=TILE_SIZE, batch=main_batch)
player_ship = player.PlayerShip(window=game_window, game_board=game_board, tile_size=TILE_SIZE, batch=main_batch)
game_objects = [player_ship]

for event_handler in player_ship.event_handlers:
    game_window.push_handlers(event_handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    to_add = []
    to_remove = []
    give_control = []

    for obj in game_objects:
        to_add.extend(obj.new_objects)
        obj.new_objects = []
        if obj.check_for_removal:
            to_remove.append(obj)

    for removal in to_remove:
        for obj in game_objects:
            if obj.can_traverse_water:
                if obj.x == removal.saved_position[0] and obj.y == removal.saved_position[1]:
                    removal.delete()
                    game_objects.remove(removal)
                    give_control.append(obj)

    if to_add:
        for obj in game_objects:
            for handler in obj.event_handlers:
                game_window.remove_handlers(handler)
        for obj in to_add:
            for handler in obj.event_handlers:
                game_window.push_handlers(handler)

    for obj in give_control:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)

    game_objects.extend(to_add)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
