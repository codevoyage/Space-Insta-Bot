import requests
import json
import os
from unidecode import unidecode


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
                # 'date':'2019-02-13'
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

    if isinstance(author, str):
        credits = " credits: " + author
    else:
        credits = ""

    caption = explanation + credits + createHashTags()

    command = "instapy -u daily_space_photos -p newspace -f " + image_url + " -t \"" + caption + "\""

    os.system(command)
    print("Posted picture of the day")
