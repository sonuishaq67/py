import requests

while True:
    try:
        x = requests.get("https://www.google.com/")
        if x.status_code != 200:
            print(x.status_code)
            continue
        print("wifi up")
        break
    except:
        pass
