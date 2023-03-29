from flask import Flask, send_from_directory
from src.routes.routes import routes
from flask_restful import Api
from bson import ObjectId
from src.controllers.post_controller import Post
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)
app.url_map.converters["ObjectId"] = ObjectId

for url, options in routes.items():
    app.add_url_rule(url, view_func=options["controller"], methods=options["methods"])

api.add_resource(Post, "/post")


@app.route("/swagger.json")
def send_swagger():
    return send_from_directory(".", "swagger.json")


# swagger setup
SWAGGER_URL = "/api/doc"
API_URL = "/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Blog api"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
