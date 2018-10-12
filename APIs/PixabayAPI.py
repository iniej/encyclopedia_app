import requests
import json
import os


pixabay_api_key = os.environ["PIXABAY_API_KEY"]


def get_image_url(search_text):

    image_url = ""

    try:
        response = requests.get("https://pixabay.com/api/?key=" + pixabay_api_key + "&q=" +
                                search_text + "&image_type=photo")

        json_resp = response.text

        image = json.loads(json_resp)

        print(image)

        if len(image["hits"]) != 0:
            image_url = image["hits"][0]["largeImageURL"]

    except requests.exceptions.HTTPError as http_error:
        print("There's a Http Error", http_error)
    except requests.exceptions.ConnectionError as conn:
        print("There's a connection error", conn)
    except requests.exceptions.Timeout as timeout:
        print("There is a timeout Error", timeout)
    except requests.exceptions.RequestException as error:
        print("Something went wrong", error)

    return image_url
