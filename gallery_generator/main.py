from pathlib import Path
import os

from dotenv import load_dotenv

from collage import CollageCreator
from images_generator import ImagesGenerator


# Loading API KEY from external file
load_dotenv(Path(".env"))
API_KEY = os.getenv("API_KEY")


def main(
    target: str,
    number: int,
    gallery_catalog: str,
    grey_scale: bool,
    gaussian: int,
    padding: int,
):
    """
    Parameters :
        target : the topic to query --> string
        number : how  many images to download --> int
        gallery_catalog : name of a directory to keep the images  --> string
        grey_scale : True or False --> bool
        gaussian : blur parameter. Value in range 0-100 --> int
        rows_and_columns : number of rows and collums in Collage --> int
        padding : gap between images --> int
    """
    p = ImagesGenerator(target, number, gallery_catalog, key=API_KEY)
    p.searching()
    p.downloading_images()
    p.converting_images(grey_scale, gaussian, (800, 800))
    collage = CollageCreator(number, padding)
    collage.run(target)


if __name__ == "__main__":
    main(
        target="LONDON",
        number=5,
        gallery_catalog="LONDON",
        grey_scale=True, 
        gaussian=1,
        padding=10
    )
