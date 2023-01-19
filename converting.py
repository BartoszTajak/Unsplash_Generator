from PIL import Image

class Images_Converter():

    def grayscale(self, input_image_path, output_image_path):
        try:
            with Image.open(input_image_path) as img:
                # converting img. to greyscale
                gray_scale = img.convert("L")
                gray_scale.save(output_image_path)
        except:
            pass


    def resize(self, input_image_path, output_image_path, new_size):
        try:
            with Image.open(input_image_path) as img:
                resized_image = img.resize(new_size)
                resized_image.save(output_image_path)
        except:
            pass

