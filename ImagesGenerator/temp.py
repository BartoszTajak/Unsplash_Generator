import urllib.request
import requests

# urllib.request.urlretrieve('www.onet.pl', "erferfer.jpg")

print(dir(requests.exceptions))


try:
    response = requests.get(
        f'https://api.unsplash.com/search/photos?page=1'
        f'&query=Poland&client_id=87RvSHeIhJyIlZ4RxFnTMs0xSgIJZ_h0jsGGtR3H_6',timeout=10)

    print(response.status_code)
    search = response.json()
    print(search)
except requests.exceptions.ConnectionError as error:
    print(error)