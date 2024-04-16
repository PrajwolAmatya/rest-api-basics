from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Clean the house", "completed": True}
]

# retrieve all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

# retrieve a specific task
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": task})

# add a new method
@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify({"task": new_task}), 201

# update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task.update(request.get_json())
    return jsonify({"task": task})

# delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_tasks(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks.remove(task)
    return jsonify({"result": "Task deleted"})


# Running the application
if __name__ == "__main__":
    app.run(debug=True)
