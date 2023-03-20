from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

# username = us.user_name()

# Find data in json
#def _find_user(user, username):
#   data = [x for x in username if x["user"]==user]
#   return data

@app.route('/item', methods=['GET'])
def item():
    _item = us.item_name()
    return jsonify(_item)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) #127.0.0.1