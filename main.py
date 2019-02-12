import requests
import json
import os
import time
from unidecode import unidecode

nasa_apod_url = 'https://api.nasa.gov/planetary/apod'


def createHashStrings():
    hashString = ''

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


for i in range(1, 31):
    date = "2015-07-" + str(i)
    response = requests.get(
        nasa_apod_url,
        params={'api_key': 'gqpGF2NFxRqYlMxbwwMRmTFyi92Qo0h9k1tNByNP',
                'date': date,
                'hd': True
                }
    )
    json_data = json.loads(response.text)

    author = json_data.get('copyright')
    explanation = json_data.get('explanation')
    image_url = json_data.get('url')

    explanation = unidecode(explanation)

    caption = cleanExplanation(explanation) + createHashStrings()

    # caption =explanation + createHashStrings()

    command = "instapy -u daily_space_photos -p newspace -f " + image_url + " -t '" + caption + "'"

    # command = "echo " + caption

    # print(command)

    os.system(command)
    time.sleep(30)
