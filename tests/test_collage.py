import unittest
import os
import os.path

from gallery_generator import images_generator
from gallery_generator.config import API_KEY
from gallery_generator.collage import CollageCreator


class TestImageGenerator(unittest.TestCase):

    def setUp(self):
        target = "Ocean"
        self.catalog_dir = "Ocean_catalog"
        self.test = images_generator.ImagesGenerator(target, 16, f"{self.catalog_dir}", API_KEY)

    # length of the list included the ID of images
    def test_images_generatos_searching(self):
        result = len(self.test.searching())
        self.assertEqual(result, 16)

    # TypeError
    def test_images_generatos_TypeError(self):
        result = self.test.searching()
        # Wrong Api Key
        self.assertRaises(TypeError, result, "Sea", 16, 'sea_catalog', '0000')
        # No results
        self.assertRaises(TypeError, result, "_______", 16, 'sea_catalog', API_KEY)

    # amount of downloaded pictures
    def test_images_generatos_amount(self):
        path = self.test.gallery_dir
        # self.test.downloading_images()
        res = os.listdir(path)
        res = [i for i in res if os.path.isfile(f"{path}\{i}")]
        self.assertEqual(len(res), 16)

    # format of downloaded pictures
    def test_images_generatos_format(self):
        path = self.test.gallery_dir
        jpg = [i for i in os.listdir(path) if "jpg" in i]
        self.assertEqual(len(jpg), 16)

    # size of downloaded pictures
    def test_images_generatos_size(self):
        path = self.test.gallery_dir
        jpg = [i for i in os.listdir(path) if os.stat(path/i).st_size != 0 and os.path.isfile(f"{path}\{i}")]
        self.assertEqual(len(jpg), 16)

    # collage.png insite
    def test_images_generatos_converting(self):
        self.test.converting_images(True, 16)
        collage = CollageCreator(16, 10, self.catalog_dir)
        collage.run()
        path = self.test.gallery_dir/'converted'
        collage_file = [i for i in os.listdir(path) if "collage.png" in i]
        self.assertEqual(len(collage_file), 1)


if __name__ == "__main__":
    unittest.main()
