from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

users_url = os.environ.get('USERS_API_URL','http://localhost:5001')

@app.get('/healthz')
def heath_check():
    return jsonify ({"status":"UP"})

@app.post('/auth/login')
def login():
    data = request.json
    print(data)
    if not data or 'username' not in data.keys():
        return 404
    response = requests.get(f'{users_url}/users')
    # print(response.json()['users'])
    for user in response.json()['users']:
        if user['name'] == data['username'] and user['email'] == data['password']:
            return 'status yeah',200
    return 'not yeah',403



@app.route('/auth/logout', methods=['POST'])
def logout():
    data = request.get_json()
    return jsonify({"success": True})
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)