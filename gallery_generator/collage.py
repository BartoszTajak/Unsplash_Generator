from math import sqrt
import os
from pathlib import Path

from PIL import Image

import config


class CollageCreator:
    def __init__(
        self,
        gallery_dir: Path,
        num_images: int = 25, 
        padding: int = 10,):
        self.gallery_dir = gallery_dir
        self.num_images = num_images
        if sqrt(num_images) % 1 != 0:
            raise ValueError("Number of images must be a square number")

        self.padding = padding

    def run(self):
        # load images
        images = [Image.open(image) for image in self.gallery_dir.iterdir()]

        # calculate dimensions
        slots = int(sqrt(self.num_images) + 1)
        padding = self.slots * self.padding
        dimension = (self.slots - 1) * 800 + padding
        size = (dimension, dimension)

        # create canvas
        white = (255, 255, 255) # rgb
        collage = Image.new("RGB", size, white)

        # dimensions in order to put image in correct place
        position_x, position_y = (self.padding, self.padding)
        number_of_foto = 1
        row = 1
        for image in images:
            collage.paste(image, (position_x, position_y))
            position_x += 800 + self.padding
            
            if number_of_foto == int(self.collage_images ** (1 / 2)) * row:
                position_y += 800 + self.padding
                position_x = self.padding
                row += 1
            
            number_of_foto += 1

        collage.save(self.gallery_dir / "collage.png", "PNG")
