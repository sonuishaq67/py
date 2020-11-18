import requests
from datetime import datetime


def main():
    url = "https://api.github.com/users/sonuishaq67/events"
    output = requests.get(url)
    lastime=output.json()[0]['created_at']
    
main()
