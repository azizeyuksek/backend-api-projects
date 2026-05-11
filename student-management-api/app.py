from flask import Flask, request, jsonify

app = Flask(__name__)

# örnek veri
students = [
    {"id": 1, "name": "Azize", "department": "Computer Engineering"},
    {"id": 2, "name": "Merve", "department": "Software Engineering"}
]

# ana sayfa
@app.route("/")
def home():
    return jsonify({"message": "Student Management API is running"})


# GET /students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# POST /students
@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    new_student = {
        "id": len(students) + 1,
        "name": data.get("name"),
        "department": data.get("department")
    }

    students.append(new_student)
    return jsonify(new_student)


# PUT /students/{id}
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.json

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["department"] = data.get("department", student["department"])
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404


# DELETE /students/{id}
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted"})

    return jsonify({"message": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)