from dotenv import load_dotenv
import os
import requests
from colored_print import log
    
def get_donald_trump():
    load_dotenv()
    
    base_url = os.getenv("DONALD_TRUMP_BASE_URL")
    url = str(base_url) + "/random/quote"
    
    print(url)

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    log.success(response_json)
    quote = response_json['value']
    # source_url = response_json['source_url']
    return quote
    
# get_donald_trump()
