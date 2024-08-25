from django.db import models
import requests

# Create your models here.

def fetch_index():
    URL = "https://raw.githubusercontent.com/codeblech/jpgram-cdn/main/index.json"
    return requests.get(URL).json()


print("caching index from cdn...")

image_index = fetch_index()
