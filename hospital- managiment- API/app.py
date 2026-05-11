from flask import Flask, request, jsonify

app = Flask(__name__)

appointments = [
    {
        "id": 1,
        "patient_name": "Merve",
        "doctor_name": "Dr. Ahmet",
        "date": "2026-05-10"
    }
]

def get_next_id():
    if not appointments:
        return 1
    return max(appt['id'] for appt in appointments) + 1

@app.route("/appointments", methods=["GET"])
def get_appointments():
    return jsonify(appointments), 200

@app.route("/appointments", methods=["POST"])
def add_appointment():
    data = request.get_json()

    required_fields = ["patient_name", "doctor_name", "date"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Eksik veri girdiniz. Lütfen ilgili alanları doldurun."}), 400

    new_appointment = {
        "id": get_next_id(),
        "patient_name": data["patient_name"],
        "doctor_name": data["doctor_name"],
        "date": data["date"]
    }

    appointments.append(new_appointment)
    return jsonify({
        "message": "Randevu başarıyla eklendi",
        "appointment": new_appointment
    }), 201

@app.route("/appointments/<int:id>", methods=["PUT"])
def update_appointment(id):
    data = request.get_json()
    
    appointment = next((appt for appt in appointments if appt["id"] == id), None)

    if appointment:
        appointment["patient_name"] = data.get("patient_name", appointment["patient_name"])
        appointment["doctor_name"] = data.get("doctor_name", appointment["doctor_name"])
        appointment["date"] = data.get("date", appointment["date"])

        return jsonify({
            "message": "Randevu güncellendi",
            "appointment": appointment
        }), 200
        
    return jsonify({"message": "Randevu bulunamadı"}), 404

@app.route("/appointments/<int:id>", methods=["DELETE"])
def delete_appointment(id):
    global appointments
    initial_length = len(appointments)
    appointments = [appt for appt in appointments if appt["id"] != id]

    if len(appointments) < initial_length:
        return jsonify({"message": "Randevu başarıyla silindi"}), 200

    return jsonify({"message": "Randevu bulunamadı"}), 404

if __name__ == "__main__":
    app.run(debug=True)