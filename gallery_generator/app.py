from pathlib import Path
import os

from gallery_generator.collage import CollageCreator
from gallery_generator.images_generator import ImagesGenerator

from dotenv import load_dotenv

# Loading API KEY from external file
load_dotenv(Path(".env"))
API_KEY = os.getenv("API_KEY")


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
    p = ImagesGenerator(target, number, gallery_dir=gallery_catalog, key=API_KEY)
    p.searching()
    p.downloading_images()
    p.converting_images(grey_scale, gaussian, (800, 800))
    collage = CollageCreator(number, padding, gallery_dir=gallery_catalog)
    collage.run(target)