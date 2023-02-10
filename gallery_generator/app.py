from gallery_generator.collage import CollageCreator
from gallery_generator.images_generator import ImagesGenerator
from gallery_generator.config import *


def main(
        target: str,
        number: int,
        gallery_catalog: Path,
        grey_scale: bool,
        gaussian: int,
        padding: int,
):
    """
    Parameters :
        target : the topic to query --> string
        number : how  many images to download --> int
        gallery_catalog : name of a directory to keep the images  --> Path
        grey_scale : True or False --> bool
        gaussian : blur parameter. Value in range 0-100 --> int
        padding : gap between images --> int
    """
    p = ImagesGenerator(search=target, num=number, gallery_dir=gallery_catalog, key=API_KEY)
    # p.searching()
    # p.downloading_images()
    p.converting_images(grey_scale, gaussian, (800, 800))
    collage = CollageCreator(number, padding, gallery_dir=gallery_catalog)
    collage.run()
