from PIL import Image, ImageFilter


class ImagesConverter():
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        try:
            with Image.open(self.input_path) as self.img:
                self.img.load()
        except Exception:
            print('Openning failed')

    # converting img. to greyscale
    def grayscale(self,):
        try:
            self.img = self.img.convert("L")
        except Exception:
            print('Converting failed')

    # converting img. to gaussian filter
    def gaussian(self, gaussian_value):
        try:
            self.img = self.img.filter(ImageFilter.GaussianBlur(gaussian_value))
        except Exception:
            print('Converting failed')

    # resizing images
    def resize(self, new_size):
        try:
            self.img = self.img.resize(new_size)
        except Exception:
            print('Converting failed')

    def save(self):
        try:
            self.img.save(self.output_path)
        except Exception:
            print('Saving failed')

