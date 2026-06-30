from flask import Flask, request, jsonify

app=Flask(__name__)

balance =[
    {
        "id":1,
        "name":"azize",
        "bank_name":"ziraat",
        "money":100
    }
]

def get_next_id():
    if not balance:
        return 1
    return max(appt["id"] for appt in balance) +1

@app.route("/balance",methods=["GET"])
def get_balance():
    return jsonify(balance),200

@app.route("/balance",methods=["POST"])
def add_balance():
    data=request.get_json()

    required_fields=["name","bank_name","money"]
    if not data  or not all(field in data for field in  required_fields):
        return jsonify({"error":"Eksik veri girdiniz.Lütfen ilgili alanları doldurun"}),40
    
    new_balance={
        "id": get_next_id(),
        "name":data["name"],
        "bank_name":data["bank_name"],
        "money":data["money"]

    }