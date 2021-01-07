from pymongo import MongoClient
import datetime

client = MongoClient("localhost", 27017)

db = client.pytests
posts = db.posts
posts.remove()
post = {
    "author": "Ishaq",
    "text": "My first blog post",
    "tags": ["mongodb", "python", "native driver"],
    "date": datetime.datetime.utcnow(),
}
post_id = posts.insert_one(post).inserted_id
print(post_id)

mulposts = [
    {
        "author": "Darth vada",
        "text": "My first blog post",
        "tags": ["mongodb", "python", "native driver"],
        "date": datetime.datetime.utcnow(),
    },
    {
        "author": "Hindu Bale",
        "text": "My first blog post",
        "tags": ["mongodb", "python", "native driver"],
        "date": datetime.datetime.utcnow(),
    },
]

posts_id = posts.insert_many(mulposts)
print(posts.count())