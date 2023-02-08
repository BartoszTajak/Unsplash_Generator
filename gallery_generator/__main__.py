import argparse
from pathlib import Path

from gallery_generator.app import main


if __name__ == "__main__":
    argparse = argparse.ArgumentParser('Script to searching , downloading and creating collage')
    argparse.add_argument\
        ('-t', "--target", help="the topic to query--> string", type=str, required=True , metavar='')
    argparse.add_argument\
        ('-n', "--number", help="how  many images to download--> int", type=int, default=25, metavar='')
    argparse.add_argument\
        ('-gc', "--gallery_catalog", help="name of a directory--> Path", type=Path, required=True, metavar='')
    argparse.add_argument\
        ('-gs', "--grey_scale", help="True or False --> bool", type=bool, default=False, metavar='')
    argparse.add_argument\
        ('-g', "--gaussian", help="blur par. Value in range 0-100--> int", type=int, default=0, metavar='')
    argparse.add_argument\
        ('-p', "--padding", help="gap between img.--> int", type=int, default=10, metavar='')
    args = argparse.parse_args()

    main(
        target=args.target,
        number=args.number,
        gallery_catalog=args.gallery_catalog,
        grey_scale=args.grey_scale,
        gaussian=args.gaussian,
        padding=args.padding,
    )
