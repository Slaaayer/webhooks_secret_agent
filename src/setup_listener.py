from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize a list to store incoming messages
messages = []

# Route to handle incoming webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    global messages
    if request.method == 'POST':
        secret_message = request.json.get('message')
        if secret_message:
            messages.append(secret_message)
            print(f"Message intercepted: {secret_message}")
        return jsonify({"status": "success", "message": "Transmission completed"}), 200

    elif request.method == 'GET':
        if messages:
            received_messages = messages.copy()  # Copy the list of messages
            messages.clear()  # Flush the list after sending the response
            return jsonify({
                "status": "success",
                "message": "Listening post active, received transmissions",
                "data": received_messages
            }), 200
        else:
            return jsonify({
                "status": "success",
                "message": "Listening post active, received no transmissions yet"
            }), 200

if __name__ == '__main__':
    app.run(port=5000)