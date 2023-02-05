from math import sqrt
from PIL import Image
from config import *

logger = logging_method(__name__)


class CollageCreator:
    def __init__(self, num_images: int = 25, padding: int = 10, gallery_dir=current_path):
        self.num_images = num_images
        self.padding = padding
        self.gallery_dir = gallery_dir
        if sqrt(num_images) % 1 != 0:
            logger.warning("Number of images must be a square number")
            raise ValueError("Number of images must be a square number")

    def run(self, target):
        # load images

        path = Path(self.gallery_dir + f'\\{target}')
        images = [Image.open(image) for image in path.iterdir() if image.is_file()]

        # calculate dimensions
        slots = int(sqrt(self.num_images) + 1)
        padding = slots * self.padding
        dimension = (slots - 1) * 800 + padding
        size = (dimension, dimension)

        # create canvas
        white = (255, 255, 255)  # rgb
        collage = Image.new("RGB", size, white)

        # dimensions in order to put image in correct place
        position_x, position_y = (self.padding, self.padding)
        number_of_foto = 1
        row = 1
        for image in images:
            collage.paste(image, (position_x, position_y))
            position_x += 800 + self.padding
            
            if number_of_foto == int(sqrt(self.num_images) ** (1 / 2)) * row:
                position_y += 800 + self.padding
                position_x = self.padding
                row += 1
            
            number_of_foto += 1
        logger.warning(f"{path} + _Converted\\Collage.png")
        collage.save(f"{path}\\{target}_Converted\\Collage.png", "PNG")
