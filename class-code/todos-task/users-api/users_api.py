from flask import Flask, request, jsonify
import os

app = Flask(__name__)

users = [
    {"id": 1, "name": "chen", "email": "1@1.com"},
    {"id": 2, "name": "david", "email": "2@2.com"},
    {"id": 3, "name": "omer", "email": "3@3.com"}
]

# base_url = os.environ.get('USERS_API_URL', 'http://localhost:5001')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "users-api"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify({"user": user})
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ["name", "email"]):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify({"user": new_user}), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)