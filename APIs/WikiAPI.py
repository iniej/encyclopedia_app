import requests
import json


def get_description(search_text):

    description = ""

    search_text.replace(" ", "_")

    try:
        params_list = {"format": "json", "action": "query", "prop": "extracts", "exintro": "",
                       "explaintext": "", "titles": search_text}

        response = requests.get("https://en.wikipedia.org/w/api.php", params=params_list)

        json_resp = response.text

        desc = json.loads(json_resp)

        page_id = list(desc["query"]["pages"])[0]

        description = desc["query"]["pages"][page_id]["extract"]

    except requests.exceptions.HTTPError as http_error:
        print("There's a Http Error", http_error)
    except requests.exceptions.ConnectionError as conn:
        print("There's a connection error", conn)
    except requests.exceptions.Timeout as timeout:
        print("There is a timeout Error", timeout)
    except requests.exceptions.RequestException as error:
        print("Something went wrong", error)

    return description

