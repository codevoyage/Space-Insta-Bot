import requests
import json
import os
from unidecode import unidecode


def createHashTags():
    hashString = ' '

    hashtags = ["#space", "#photography", "#nasa", "#universe", "#galaxy", "#nightsky", "#spacefacts", "#stars"]
    for i in range(len(hashtags)):
        hashString = hashString + " " + hashtags[i]

    return hashString


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
                'hd': True
                }
    )
    json_data = json.loads(response.text)

    return json_data


def post_picture_insta():
    data = get_picture_nasa()
    author = data.get('copyright')
    explanation = data.get('explanation')
    image_url = data.get('url')

    explanation = unidecode(explanation)

    credits = " credits: " + author

    # caption = cleanExplanation(explanation) + credits + createHashTags()

    caption = explanation + credits + createHashTags()


    command = "instapy -u daily_space_photos -p newspace -f " + image_url + " -t '" + caption + "'"

    print(command)

    # os.system(command)