import pytmx
from pytmx.util_pygame import load_pygame

# Load the TMX map
tmx_data = load_pygame("level1.tmx")

# Render the map
for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for x, y, gid in layer:
            image = tmx_data.get_tile_image_by_gid(gid)
            if image:
                screen.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
