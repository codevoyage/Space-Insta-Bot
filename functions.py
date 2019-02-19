import requests
import json
import os
from unidecode import unidecode
import urllib.request
from PIL import Image


def createHashTags():
    hashtags = " #science #sciencefacts #space #physics #universe #nasa #astronomy" \
               " #stars #sky #galaxy #cosmos #photography #knowledge #facts"

    return hashtags


def cleanExplanation(explanation):
    specialChars = ['(', ')', ]
    # ! ? $ % $  # & * ( ) blank tab | ' ; " < > \ ~ ` [ ] { }

    result = explanation.replace('\'', '')

    for i in range(len(specialChars)):
        char = specialChars[i]
        if char in result:
            result = result.replace(char, "\\" + char)

    return result


def get_picture_nasa():
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(
        nasa_apod_url,
        params={'api_key': 'gqpGF2NFxRqYlMxbwwMRmTFyi92Qo0h9k1tNByNP',
                'hd': True,
                'date': '2019-02-18'
                }
    )
    json_data = json.loads(response.text)

    return json_data


def download_image(url):
    urllib.request.urlretrieve(url, "photo.jpg")


def fix_aspect_ratio():
    insta_min_ratio = 0.8
    insta_max_ratio = 1.91
    original = Image.open('photo.jpg')
    width, height = original.size

    original_aspect_ratio = width / height

    final_image = "photo.jpg"

    if original_aspect_ratio <= insta_min_ratio:
        print("Photo is too long, making changes")
        original.show()
        crop_height = width / insta_min_ratio
        box = (0, 0, crop_height, crop_height)
        cropped_image = original.crop(box)
        cropped_image.save('cropped.jpg')
        cropped = Image.open('cropped.jpg')
        cropped.show()
        final_image = "cropped.jpg"
    elif insta_max_ratio <= original_aspect_ratio:
        print("Photo is too wide, making changes")
        crop_width = insta_max_ratio * height
        final_image = "cropped.jpg"

    return final_image


def clean_data():
    data = get_picture_nasa()
    author = data.get('copyright')
    explanation = data.get('explanation')

    explanation = unidecode(explanation)

    if isinstance(author, str):
        credits = " credits: " + author
    else:
        credits = ""

    caption = explanation + credits + createHashTags()

    download_image(data.get('url'))
    image = fix_aspect_ratio()

    post_picture_insta(image, caption)


def post_picture_insta(image, caption):
    command = "instapy -u daily_space_photos -p newspace -f" + image + " -t \"" + caption + "\""

    # os.system(command)
    print("Ran command to post picture of the day")


def start():
    clean_data()
