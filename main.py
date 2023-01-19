import urllib.request
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from converting import Images_Converter
import time

#Loading API KEY from external file
load_dotenv(Path(".env"))
API_KEY = os.getenv("API_KEY")


class Images_Generator():
    """
    Class to search any images by using API Unsplash and then convert if needed
    Before the first use API Key is neede from https://unsplash.com/developers
    Parameters :
    search : the item we are looking for --> string
    num : how  many images to download --> int
    dic : name of a directory to save  --> string
    For Example:
    p = Images_Generator('NewYork',20,'MyFirstCollecion' )
    """

    def __init__(self, search : str, num : int, dic : str ):
        self.search = search
        self.num = num
        self.dic = dic


    # Method to search photos on https://api.unsplash.com then  return list includes ID of photos
    def searching(self):
        id_photos_list = []
        for numer_of_page in range(1, 10):
            try:
                response = requests.get(
                    f'https://api.unsplash.com/search/photos?page={numer_of_page}&query={self.search}&client_id={API_KEY}')
                search = response.json()
                for i in range(10):
                    id_photos_list.append(search['results'][i]['id'])
                    if len(id_photos_list) == self.num:
                        return id_photos_list
            except:
                pass

    # Method to download images by ID Photos from searching()
    def downloading_images(self):
        os.makedirs(fr"images\{self.dic}", exist_ok=True)
        try:
            for Photo_ID in self.searching():
                link_to_img = requests.get(
                    f'https://api.unsplash.com/photos/{Photo_ID}/download?ixid=MubhI3_D8BEN79D7Xli0kAc6Ol7HaNe0gkR3IAkuoDw&client_id={API_KEY}')
                link_to_img = link_to_img.json()
                print(link_to_img['url'])
                urllib.request.urlretrieve(link_to_img['url'], f"images/{self.dic}/{Photo_ID}.jpg")
        except:
            print('downloading failed')



    def converting_images(self,grey_scale : bool ):
        # creating a new catalog for converted photos
        converted_path = fr"images\{self.dic}\{self.dic}" + "_Converted"
        os.makedirs(converted_path, exist_ok=True)

        # Creating a new object in order to convert files
        p = Images_Converter()
        list_of_photos = os.listdir(f"images\{self.dic}")
        if grey_scale == True:
            for photo in list_of_photos:
             p.grayscale(f"images\{self.dic}\{photo}", f'{converted_path}\{photo}')
        else:
            pass



if __name__ == "__main__":
    p = Images_Generator('PYTHON',10,'PYTHON_CODE')
    p.searching()
    p.downloading_images()
    p.converting_images(True,)









