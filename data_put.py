from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def update():
    # id = request.form.get('id')
    user = request.form.get('username')
    passwd = request.form.get('password')
    name = request.form.get('name')

    _user = us.user_name()
    data = [x for x in _user if x["user"]==user]

    if data:
        us.update_user(user,passwd,name)
        return jsonify({'message': 'Update Successfully'}), 200
    else:
        return jsonify({'message': 'Fail to update.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1