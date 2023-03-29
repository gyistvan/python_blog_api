import os
import pymongo
from jinja2 import Environment, FileSystemLoader
from src.db.db import db


def home():
    env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "../templates"))
    )
    template = env.get_template("home.html")
    collection = db["blog_app"]
    posts = list(collection.find({}).limit(20).sort("created_at", pymongo.DESCENDING))
    for post in posts:
        post["_id"] = str(post["_id"])
    output = template.render({"posts": posts})
    return output
