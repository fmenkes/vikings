import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

tileset = pyglet.resource.image('tiles.png')
water_tile = tileset.get_region(0, 320, 16, 16)
ship_tile = tileset.get_region(32, 320, 16, 16)
grass_tile = tileset.get_region(32, 352, 16, 16)
sand_tile = tileset.get_region(64, 352, 16, 16)
mountain_tile = tileset.get_region(96, 352, 16, 16)

