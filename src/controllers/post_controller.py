from flask import jsonify, request
from flask_restful import Resource
from flask_restful_swagger import swagger
from src.db.db import db
from src.types.Post_type import Post
from bson import ObjectId
from datetime import datetime


class Post(Resource):
    def serialize_request_body(self, fields, data, is_required):
        error_messages = {}

        for field in fields:
            if is_required:
                if field not in data:
                    error_messages[field] = field + " is required"
            else:
                if field in data:
                    error_messages[field] = field + " is restricted"

        return error_messages

    def postHandler2(self, id):
        if request.method == "GET":
            return self.getById(id=id)
        elif request.method == "PATCH":
            return self.updatePost(id=id)
        else:
            return {"message": "The method is not allowed for the requested URL."}

    def postHandler(self):
        if request.method == "GET":
            return self.getAll()
        elif request.method == "POST":
            return self.createPost()
        else:
            return {"message": "The method is not allowed for the requested URL."}

    def getAll(self):
        """
        Get all posts
        """
        collection = db["blog_app"]
        posts = list(collection.find({}))
        for post in posts:
            post["_id"] = str(post["_id"])

        return posts

    def getById(self, id):
        """
        Get a post by Id
        """

        collection = db["blog_app"]
        _id = ObjectId(id)
        post = collection.find_one(filter={"_id": _id})

        if post is None:
            return jsonify({"message": "Post not found"}), 404

        post["_id"] = str(post["_id"])

        return jsonify(post), 200

    def createPost(self):
        """
        Create a post
        """
        collection = db["blog_app"]
        data = request.json
        required_fields = [
            "title",
            "image_url",
            "short_text",
            "long_text",
            "author_id",
            "author_name",
        ]
        error_messages = self.serialize_request_body(required_fields, data, True)
        if len(error_messages) > 0:
            return jsonify(error_messages), 400

        dt = str(round(datetime.now().timestamp()))
        data["created_at"] = dt
        collection.insert_one(data)
        data["_id"] = str(data["_id"])

        return jsonify(data)

    def updatePost(self, id):
        object_id = ObjectId(id)
        filter = {"_id": object_id}
        restricted_fields = ["_id", "id", "created_at"]
        data = request.json
        error_messages = self.serialize_request_body(restricted_fields, data, False)
        if len(error_messages) > 0:
            return jsonify(error_messages), 400
        collection = db["blog_app"]
        update = {"$set": data}
        collection.update_one(filter, update)

        return self.getById(id=id)
