from django.db import models
import requests

# Create your models here.

def fetch_index():
    URL = "https://raw.githubusercontent.com/codeblech/jpgram-cdn/main/index.json"
    return requests.get(URL).json()
