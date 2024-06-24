# tile_generator.py
import os
import rasterio
import numpy as np
from rasterio.windows import Window

def create_tiles(geotiff_path, output_dir, tile_size=256):
    with rasterio.open(geotiff_path) as src:
        width = src.width
        height = src.height

        os.makedirs(output_dir, exist_ok=True)

        for i in range(0, width, tile_size):
            for j in range(0, height, tile_size):
                window = Window(i, j, tile_size, tile_size)
                transform = src.window_transform(window)
                tile = src.read(1, window=window)

                tile_filename = os.path.join(output_dir, f'tile_{i}_{j}.tif')
                with rasterio.open(
                    tile_filename, 'w',
                    driver='GTiff',
                    height=tile.shape[0],
                    width=tile.shape[1],
                    count=1,
                    dtype=tile.dtype,
                    crs=src.crs,
                    transform=transform
                ) as dst:
                    dst.write(tile, 1)

geotiff_path = 'path/to/your/geotiff.tif'
output_dir = 'path/to/output/tiles'
create_tiles(geotiff_path, output_dir)
