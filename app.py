from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data
users = {"123-45-6789": {"dob": "1990-01-01"}, "987-65-4321": {"dob": "1985-05-12"}}


@app.get("/")
def health():
    return jsonify({"message": "Healthy"}), 200


@app.route("/authenticate", methods=["POST"])
def authenticate():
    return jsonify({"name": "My name is MIKE"}), 200


if __name__ == "__main__":
    app.run(debug=True)
