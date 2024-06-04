from dotenv import load_dotenv
import os
import requests
from colored_print import log
    
def get_bacon_ipsum():
    load_dotenv()
    
    base_url = os.getenv("BACON_IPSUM_BASE_URL")
    url = str(base_url) + "/?type=meat-and-filler&paras=5&sentences=0&start-with-lorem=1&format=json"
    
    print(url)

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    # modified_string = original_string[2:-2]
    bacon_ipsum = str(response_json)[2:-2]
    log.success(bacon_ipsum)
    # source_url = response_json['source_url']
    return bacon_ipsum
    
get_bacon_ipsum()
