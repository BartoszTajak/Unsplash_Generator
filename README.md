# About The Project

Program to create a collage based on photos downloaded from https://unsplash.com/. One can search for any images and, based on them, make a collage with various sizes: 3x3, 4x4, etc. Each new request to API makes a new catalog where photos are saved. There are also available additional features like grey scale and blurring.

## Setup
* Register at Unsplash and save the API KEY to `.env` file.

```bash
echo API_KEY=$KEY > .env
``` 

* Install all packages
```bash
pip install -e .
```

## Usage
```python
>>> import gallery_generator
>>> gallery_generator.run(target="LONDON", number=16, gallery_catalog="LONDON", grey_scale=True,  gaussian=1, padding=10)
```

## Command-line usage
```bash
usage: Script to searching , downloading and creating collage [-h] -t  [-n] -gc  [-gs] [-g] [-p]

options:
  -h, --help            show this help message and exit
  -t , -target          the topic to query--> string
  -n , -number          how many images to download--> int
  -gc , -gallery_catalog 
                        name of a directory--> string
  -gs , -grey_scale     True or False --> bool
  -g , -gaussian        blur par. Value in range 0-100--> int
  -p , -padding         gap between img.--> int
```

```bash
python3 gallery_generator/main.py \
    -t cats \
    -n 10 \
    -gc out \
    -g 20 \
    -p 2
```

## Sample collages 

![App Screenshot](https://i.postimg.cc/HxJdWbq9/327117086-905430134218755-499799057236371167-n.png)
##
[![327003217-1168683380499511-3512832973350874697-n.png](https://i.postimg.cc/59LWP9by/327003217-1168683380499511-3512832973350874697-n.png)](https://postimg.cc/14mdXQg1)

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bartek-tajak-aa8662b0/)


## Documentation

[Documentation](https://unsplash.com/documentation)
