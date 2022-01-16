
from app import app
import controllers


@app.route("/", methods=['post', 'get'])
def login():
    return controllers.read_user()


@app.route("/users")
def view_users():
    return controllers.get_all_users()
