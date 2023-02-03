from PIL import Image, ImageFilter


class ImagesConverter():
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        try:
            with Image.open(self.input_path) as self.img:
                self.img.load()
        except Exception as error:
            print(error)

    # converting img. to greyscale
    def grayscale(self):
        try:
            self.img = self.img.convert("L")
        except Exception as error:
            print('grayscale error :', error)

    # converting img. to gaussian filter
    def gaussian(self, gaussian_value):
        try:
            self.img = self.img.filter(ImageFilter.GaussianBlur(gaussian_value))
        except Exception as error:
            print('gaussian error : ', error)

    # resizing images
    def resize(self, new_size):
        try:
            self.img = self.img.resize(new_size)
        except Exception as error:
            print('resize error : ', error)

    def save(self):
        try:
            self.img.save(self.output_path)
        except Exception as error:
            print('save error : ', error)
