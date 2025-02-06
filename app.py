from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data
users = {"123-45-6789": {"dob": "1990-01-01"}, "987-65-4321": {"dob": "1985-05-12"}}


@app.get("/")
def health():
    return jsonify({"message": "Healthy"}), 200


@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.json
    ssn = data.get("ssn")
    dob = data.get("dob")

    if not ssn or not dob:
        return jsonify({"message": "SSN and DOB are required"}), 400

    user = users.get(ssn)
    if user and user["dob"] == dob:
        return jsonify({"message": "Authenticated"}), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401


if __name__ == "__main__":
    app.run(debug=True)
