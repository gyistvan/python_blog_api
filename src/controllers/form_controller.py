from flask import request
from src.db.db import db


def form():
    collection = db["python_test_collection"]
    result = collection.insert_one({"name": request.form["name"]})

    return f"Inserted document with ID: {result.inserted_id}"
