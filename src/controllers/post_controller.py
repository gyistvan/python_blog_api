from flask import jsonify, request
from flask_restful import Resource
from flask_restful_swagger import swagger
from src.db.db import db
from src.types.Post_type import Post
from bson import ObjectId
from datetime import datetime


class Post(Resource):
    @swagger.operation(
        notes="Get all posts",
        responseClass=Post.__name__,
        nickname="getPosts",
        parameters=[
            {
                "name": "message_id",
                "description": "The ID of the message to retrieve",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "path",
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Message found"},
            {"code": 404, "message": "Message not found"},
        ],
    )
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
        dt = str(round(datetime.now().timestamp()))
        data["created_at"] = dt
        collection.insert_one(data)
        data["_id"] = str(data["_id"])

        return jsonify(data)

    def updatePost(self, id):
        object_id = ObjectId(id)
        filter = {"_id": object_id}

        collection = db["blog_app"]
        update = {"$set": request.json}
        result = collection.update_one(filter, update)

        return jsonify(result)
