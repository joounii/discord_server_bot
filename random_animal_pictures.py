from dotenv import load_dotenv
import os
import requests
from colored_print import log
    
def get_cat_image():
    load_dotenv()
    
    base_url = os.getenv("CAT_PICTURE_BASE_URL")
    url = str(base_url) + "/images/search"
    print(url)

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_list = response.json()
    image = response_list[0]['url']
    return image

def get_dog_image():
    load_dotenv()
    
    base_url = os.getenv("RANDOM_DOG_BASE_URL")
    url = str(base_url) + "/woof.json"
    response = requests.get(url)
    # Print the response
    response_json = response.json()
    image = response_json['url']
    return image

def get_duck_image():
    load_dotenv()
    
    base_url = os.getenv("RANDOM_DUCK_BASE_URL")
    url = str(base_url) + "/random"
    response = requests.get(url)
    # Print the response
    response_json = response.json()
    image = response_json['url']
    return image