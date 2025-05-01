from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Sample todos database
todos = [
    {"id": 1, "user_id": 1, "title": "Learn Kubernetes", "completed": False},
    {"id": 2, "user_id": 1, "title": "Study pod networking", "completed": True},
    {"id": 3, "user_id": 2, "title": "Practice with services", "completed": False},
    {"id": 4, "user_id": 3, "title": "Deploy multi-container app", "completed": False}
]

# Get the API URLs from environment variables
auth_url = os.environ.get('AUTH_API_URL', 'http://localhost:5002')
users_url = os.environ.get('USERS_API_URL', 'http://localhost:5001')

@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify({"status": "UP", "service": "todos-api"})

@app.route('/todos', methods=['GET'])
def get_todos():
    # Get user_id from query parameter
    user_id = request.args.get('user_id', type=int)
    
    if user_id:
        # Filter todos by user_id
        user_todos = [todo for todo in todos if todo["user_id"] == user_id]
        return jsonify({"todos": user_todos})
    else:
        # Return all todos if no user_id specified
        return jsonify({"todos": todos})

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        return jsonify({"todo": todo})
    return jsonify({"error": "Todo not found"}), 404

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or "title" not in data or "user_id" not in data:
        return jsonify({"error": "Missing title or user_id"}), 400
    
    # Verify user exists
    try:
        response = requests.get(f"{users_url}/users/{data['user_id']}")
        if response.status_code != 200:
            return jsonify({"error": "User not found"}), 404
    except requests.RequestException:
        return jsonify({"error": "Could not verify user"}), 503
    
    new_todo = {
        "id": len(todos) + 1,
        "user_id": data["user_id"],
        "title": data["title"],
        "completed": False
    }
    todos.append(new_todo)
    return jsonify({"todo": new_todo}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    data = request.get_json()
    if "title" in data:
        todo["title"] = data["title"]
    if "completed" in data:
        todo["completed"] = data["completed"]
    
    return jsonify({"todo": todo})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo_index = next((i for i, t in enumerate(todos) if t["id"] == todo_id), None)
    if todo_index is None:
        return jsonify({"error": "Todo not found"}), 404
    
    deleted_todo = todos.pop(todo_index)
    return jsonify({"success": True, "deleted": deleted_todo})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=True)