from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(USERS.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user(username):
    user = USERS.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404
    

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()

    if not user_data or "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    user_name = user_data.get("username")
    if user_name in USERS:
        return jsonify({"error": "Username already exists"}), 409
    
    USERS[user_name] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201
    

if __name__ == "__main__":
    app.run()
