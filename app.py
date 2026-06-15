# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)
todos = [
    {"id": 1, "task": "Learn Git", "done": True},
    {"id": 2, "task": "Build a pipeline", "done": False},
]

@app.route("/")
def home():
    return jsonify({"message": "Todo API is running", "version": "1.0"})

@app.route("/todos")
def get_todos():
    return jsonify(todos)

@app.route("/todos/<int:todo_id>")
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    return jsonify(todo) if todo else (jsonify({"error": "not found"}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)