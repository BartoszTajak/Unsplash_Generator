import os
import urllib.request
import requests
from converting import ImagesConverter
from config import *

logger = logging_method(__name__)


class ImagesGenerator:
    """
    Class to search any images by using API Unsplash and then convert if needed
    Before the first use API Key is neede from https://unsplash.com/developers
    For Example:
    main('Warsaw', 6, 'Warsaw', True, 20, 5, 30)
    Parameters :
    target : the item we are looking for --> string
    number : how  many images to download --> int
    catalog : name of a directory to save  --> string
    grey_scale : True or False --> bool
    gaussian : value in range 0-100 --> int
    rowsAndColumns : number of rows and collums in Collage --> int
    padding : gap between images --> int
    """

    def __init__(self, search: str, num: int, dic: str, key: str):
        self.search = search
        self.num = num
        self.dic = dic
        self.path = f"{current_path}{self.dic}"
        self.key = key

    # Method to search photos on https://api.unsplash.com then  return list includes ID of photos
    def searching(self):
        id_photos_list = []
        for numer_of_page in range(1, 10):
            try:
                response = requests.get(
                    f"https://api.unsplash.com/search/photos?page={numer_of_page}"
                    f"&query={self.search}&client_id={self.key}"
                )
                if response.status_code == 401:
                    logger.warning(f"{response.json()['errors'][0]} {response.status_code}")
                    raise ValueError(f"{response.json()['errors'][0]} {response.status_code}")
                print(response.json())
                if response.json()["total"] < self.num:
                    logger.warning("No Results !!!")
                    raise ValueError("No Results !!!")
                search = response.json()
                for i in range(10):
                    id_photos_list.append(search["results"][i]["id"])
                    if len(id_photos_list) == self.num:
                        return id_photos_list
            except Exception as error:
                logger.warning(error)
                raise ValueError(error)

    # Method to download images by ID Photos from searching()
    def downloading_images(self):
        os.makedirs(self.path, exist_ok=True)
        try:
            for Photo_ID in self.searching():
                link_to_img = requests.get(
                    f"https://api.unsplash.com/photos/{Photo_ID}"
                    f"/download?ixid=MubhI3_D8BEN79D7Xli0kAc6Ol7HaNe0gkR3IAkuoDw&client_id={self.key}"
                )
                link_to_img = link_to_img.json()
                urllib.request.urlretrieve(
                    link_to_img["url"], self.path + "\\" + f"{Photo_ID}.jpg"
                )
        except Exception as error:
            logger.warning(error)

    def converting_images(self, grey_scale: bool = False, gaussian: int = 0, *resize):
        # creating a new catalog for converted photos
        converted_path = self.path + "\\" + self.dic + "_Converted"
        os.makedirs(converted_path, exist_ok=True)
        # list of photos in catalog
        list_of_photos = os.listdir(self.path)
        logger.info(list_of_photos)

        # converting photos
        for photo in list_of_photos:
            # Creating a new object in order to convert files
            new_photo = ImagesConverter(
                self.path + "\\" + photo, f"{converted_path}\\{photo}"
            )
            if grey_scale is True:
                new_photo.grayscale()
            if gaussian != 0:
                new_photo.gaussian(gaussian)
            if resize != ():
                new_photo.resize(resize[0])
            new_photo.save()
