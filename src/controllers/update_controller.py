from bson import ObjectId
from flask import request
from src.db.db import db


def update(id):
    print(type(id))
    collection = db["blog_app"]
    object_id = ObjectId(id)
    filter = {"_id": object_id}
    update = {"$set": request.json}
    result = collection.update_one(filter, update)

    return f"Updated document with ID: {result.upserted_id}"
