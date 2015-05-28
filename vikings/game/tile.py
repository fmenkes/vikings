import pyglet
import resources


class Tile(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(Tile, self).__init__(*args, **kwargs)


class WaterTile(Tile):
    def __init__(self, *args, **kwargs):
        super(WaterTile, self).__init__(img=resources.water_tile, *args, **kwargs)


class GrassTile(Tile):
    def __init__(self, *args, **kwargs):
        super(GrassTile, self).__init__(img=resources.grass_tile, *args, **kwargs)


class SandTile(Tile):
    def __init__(self, *args, **kwargs):
        super(SandTile, self).__init__(img=resources.sand_tile, *args, **kwargs)


class MountainTile(Tile):
    def __init__(self, *args, **kwargs):
        super(MountainTile, self).__init__(img=resources.mountain_tile, *args, **kwargs)