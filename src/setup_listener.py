from flask import Flask, request, jsonify

app = Flask(__name__)
# Route to handle incoming webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        secret_message = request.json.get('message')
        global message
        message = secret_message
        print(f"Message intercepted: {secret_message}")
        return jsonify({"status": "success", "message": "Transmission completed"}), 200
    elif request.method == 'GET':
        if 'message' in globals():
            return jsonify({"status": "success", "message": f"Listening post active, received transmission {message}"}), 200
        else:
            return jsonify({"status": "success", "message": "Listening post active, received no transmissions yet"}), 200
if __name__ == '__main__':
    app.run(port=5000)