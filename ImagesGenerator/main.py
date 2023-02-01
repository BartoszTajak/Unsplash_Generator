import sys
import urllib.request
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from converting import ImagesConverter
from Collage import CollageCreator
current_path = os.path.dirname(os.getcwd())


# Loading API KEY from external file
load_dotenv(Path(".env"))
API_KEY = os.getenv("API_KEY")


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

    def __init__(self, search: str, num: int, dic: str):
        self.search = search
        self.num = num
        self.dic = dic
        # Executing method
        self.searching()
        # self.downloading_images()

    # Method to search photos on https://api.unsplash.com then  return list includes ID of photos
    def searching(self):
        id_photos_list = []
        for numer_of_page in range(1, 10):
            try:
                response = requests.get(
                    f'https://api.unsplash.com/search/photos?page={numer_of_page}'
                    f'&query={self.search}&client_id={API_KEY}')
                if response.status_code == 401:
                    sys.exit(f"{response.json()['errors'][0]} {response.status_code}")
                if response.json()['total'] == 0:
                    raise ValueError ('No Results !!!')
                search = response.json()
                for i in range(10):
                    id_photos_list.append(search['results'][i]['id'])
                    if len(id_photos_list) == self.num:
                        return id_photos_list
            except requests.exceptions.ConnectionError as error:
                print(error)
                sys.exit('Connection Error')
            except Exception as error:
                sys.exit(f'Something wrong : {error}')

    # Method to download images by ID Photos from searching()
    def downloading_images(self):
        os.makedirs(current_path + f"\images\{self.dic}", exist_ok=True)
        try:
            for Photo_ID in self.searching():
                link_to_img = requests.get(
                    f'https://api.unsplash.com/photos/{Photo_ID}'
                    f'/download?ixid=MubhI3_D8BEN79D7Xli0kAc6Ol7HaNe0gkR3IAkuoDw&client_id={API_KEY}')
                link_to_img = link_to_img.json()
                # print(link_to_img)
                # print(link_to_img['url'])
                urllib.request.urlretrieve(link_to_img['url'], current_path + f"\images/{self.dic}/{Photo_ID}.jpg")
        except Exception as error:
            print(f'Error references to : {error}')

    def converting_images(self, grey_scale: bool = False, gaussian: int = 0, *resize):
        # creating a new catalog for converted photos
        converted_path = current_path+fr"\images\{self.dic}\{self.dic}" + "_Converted"
        os.makedirs(converted_path, exist_ok=True)
        # list of photos in catalog
        list_of_photos = os.listdir(current_path + f"\images\{self.dic}")

        # converting photos
        for photo in list_of_photos:
            # Creating a new object in order to convert files
            new_photo = ImagesConverter(current_path + f"\images\{self.dic}\{photo}", f'{converted_path}\{photo}')
            if grey_scale is True:
                new_photo.grayscale()
            if gaussian != 0:
                new_photo.gaussian(gaussian)
            if resize != ():
                new_photo.resize(resize[0])
            new_photo.save()


def main(target: str, number: int, catalog: str, grey_scale: bool, gaussian: int,rows_and_columns: int, padding: int):
    p = ImagesGenerator(target, number, catalog)
    p.converting_images(grey_scale, gaussian, (800, 800))
    collage = CollageCreator(rows_and_columns, padding)
    collage.main(catalog)


if __name__ == "__main__":
    main('dfgdfg', 5, 'France', True, 1, 6, 10)
