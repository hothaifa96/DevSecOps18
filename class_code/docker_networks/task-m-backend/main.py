from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# hostname = os.environ("HOST")
# Connect to MongoDB
client = MongoClient('mongodb://tasks-db:27017/') # replace with container ip -172.21.0.3
db = client['tasksdb']
tasks_collection = db['tasks']

# Routes
@app.route('/', methods=['GET'])
def home():
    return "Tasks API is running!"

# Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = list(tasks_collection.find())
        # Convert ObjectId to string for JSON serialization
        for task in tasks:
            task['_id'] = str(task['_id'])
        return jsonify(tasks)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Create a task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        task = {
            'title': data.get('title'),
            'description': data.get('description'),
            'completed': data.get('completed', False),
            'createdAt': datetime.datetime.now()
        }
        result = tasks_collection.insert_one(task)
        # Return the created task
        created_task = tasks_collection.find_one({"_id": result.inserted_id})
        created_task['_id'] = str(created_task['_id'])
        return jsonify(created_task), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

# Delete a task
@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        tasks_collection.delete_one({"_id": ObjectId(task_id)})
        return jsonify({"message": "Task deleted"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Update a task
@app.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.json
        update_data = {}
        
        if 'title' in data:
            update_data['title'] = data['title']
        if 'description' in data:
            update_data['description'] = data['description']
        if 'completed' in data:
            update_data['completed'] = data['completed']
        
        tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": update_data}
        )
        
        updated_task = tasks_collection.find_one({"_id": ObjectId(task_id)})
        updated_task['_id'] = str(updated_task['_id'])
        return jsonify(updated_task)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)