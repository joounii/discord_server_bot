from dotenv import load_dotenv
import os
import requests
from colored_print import log
import discord
from discord import app_commands
    
def generate_qr_code(link):
    load_dotenv()
    
    base_url = os.getenv("QR_CODE_BASE_URL")
    url = str(base_url) + f"/create-qr-code/?size=1000x1000&data={link}"
    log.success(url)

    # A GET request to the API
    response = requests.get(url)
    log.warn(response)
    log.info(response.headers['Content-Type'])
    
    return response.content
    
# generate_qr_code("test")