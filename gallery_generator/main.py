from pathlib import Path
import os
import argparse
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
        padding : gap between images --> int
    """
    p = ImagesGenerator(target, number, gallery_catalog, key=API_KEY)
    p.searching()
    p.downloading_images()
    p.converting_images(grey_scale, gaussian, (800, 800))
    collage = CollageCreator(number, padding)
    collage.run(target)


if __name__ == "__main__":

    # argparse = argparse.ArgumentParser('Script to searching , downloading and creating collage')
    # argparse.add_argument\
    #     ('-t', "-target", help="the topic to query--> string", type=str, required=True , metavar='')
    # argparse.add_argument\
    #     ('-n', "-number", help="how  many images to download--> int", type=int, default=25, metavar='')
    # argparse.add_argument\
    #     ('-gc', "-gallery_catalog", help="name of a directory--> string", type=str, required=True, metavar='')
    # argparse.add_argument\
    #     ('-gs', "-grey_scale", help="True or False --> bool", type=bool, default=False, metavar='')
    # argparse.add_argument\
    #     ('-g', "-gaussian", help="blur par. Value in range 0-100--> int", type=int, default=0, metavar='')
    # argparse.add_argument\
    #     ('-p', "-padding", help="gap between img.--> int", type=int, default=10, metavar='')
    # argparse.add_argument('-t','--test',  metavar='',action='append')

    # args = argparse.parse_args()




    # main(
        # target=args.target,
        # number=args.number,
        # gallery_catalog=args.gallery_catalog,
        # grey_scale=args.grey_scale,
        # gaussian=args.gaussian,
        # padding=args.padding,
        # testt = args.test,

    main(target="LONGON", number=16, gallery_catalog="LONDON", grey_scale=True, gaussian=1,
                               padding=10)
    # )
