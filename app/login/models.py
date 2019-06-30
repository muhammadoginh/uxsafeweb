from flask_login import UserMixin
import requests

from app import login_manager


class User(UserMixin):

    def __init__(self, user_json):
        self.user_json = user_json

    # Overriding get_id is required if you don't have the id property
    # Check the source code for UserMixin for details
    def get_id(self):
        object_id = self.user_json.get('id')
        return str(object_id)


@login_manager.user_loader
def user_loader(id):
    # api-endpoint 
    URL = "http://localhost:3000/api/users"
    content = requests.get(URL)
    users = content.json()

    users = users['users']
    user_json = users
    return User(user_json)
