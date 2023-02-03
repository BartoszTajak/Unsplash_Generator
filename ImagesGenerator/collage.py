from PIL import Image
import os
import config


class CollageCreator():
    def __init__(self, collage_images: int = 5, padding: int = 10):
        self.collage_images = collage_images ** 2
        self.padding = padding

    def main(self, place):
        config.current_path = config.current_path + f'{place}\\{place}'
        path = config.current_path + "_Converted"
        list_of_photos = os.listdir(path)

        # dimension of frame (size of pictures and padding)
        one_side_dimension = int(
            (self.collage_images ** (1 / 2) + 1) * self.padding + (self.collage_images ** (1 / 2) * 800))
        size_of_frame = (one_side_dimension, one_side_dimension)

        # creating an empty white  picture like a base for other images
        rbg = (255, 255, 255)
        img = Image.new("RGB", size_of_frame, rbg)

        # dimensions in order to put image. in correct place
        position_x, position_y = (self.padding, self.padding)
        number_of_foto = 1
        row = 1
        for image in list_of_photos:
            image_one = Image.open(config.current_path + f"_Converted\\{image}")
            img.paste(image_one, (position_x, position_y))
            position_x += 800 + self.padding
            if number_of_foto == int(self.collage_images ** (1 / 2)) * row:
                position_y += 800 + self.padding
                position_x = self.padding
                row += 1
            number_of_foto += 1

        img.save(config.current_path + "_Converted\\Collage.png", "PNG")
