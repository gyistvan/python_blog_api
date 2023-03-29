from src.controllers.home_controller import home
from src.controllers.form_controller import form
from src.controllers.json_controller import json
from src.controllers.update_controller import update
from src.controllers.post_controller import Post

post = Post()

routes = {
    "/": {
        "methods": ["GET"],
        "controller": home,
    },
    "/form": {
        "methods": ["POST"],
        "controller": form,
    },
    "/json": {
        "methods": ["POST"],
        "controller": json,
    },
    "/update/<string:id>": {"methods": ["PUT"], "controller": update},
    "/posts/": {"methods": ["GET", "POST"], "controller": post.postHandler},
    "/posts/<string:id>": {
        "methods": ["GET", "PATCH"],
        "controller": post.postHandler2,
    },
}
