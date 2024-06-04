from dotenv import load_dotenv
import os
import requests
from colored_print import log
    
def get_usless_fact():
    load_dotenv()
    
    base_url = os.getenv("USLESS_FACTS_BASE_URL")
    url = str(base_url) + "/random"
    print(url)

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    log.success(response_json)
    fact = response_json['text']
    source_url = response_json['source_url']
    return fact, source_url
