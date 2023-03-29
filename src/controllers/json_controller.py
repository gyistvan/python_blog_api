from flask import request
from src.db.db import db


def json():
    data = request.json
    collection = db["python_test_collection_from_json"]
    result = collection.insert_one({"name": data["name"]})

    return f"Inserted document with ID: {result.inserted_id}"
