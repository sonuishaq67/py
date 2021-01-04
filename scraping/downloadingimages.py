import requests
from io import BytesIO
from PIL import Image

# r = requests.get("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg")
r = requests.get(
    "https://lh3.googleusercontent.com/proxy/bzh05xhldnE7ZQDB-jDmgLikkjI6zh7gQxnSQQA0qPG9k6UUUEn7cBsD9Bzi4XMOen-gdhd_M1gMQY8fvjzHbTo6gszgmZUk-bDLc9VhWo0AnOJ9Y5AiiZWsTxI"
)

print(r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = f"./image." + image.format
try:
    image.save(path, image.format)
except:
    print("Cannot save image")