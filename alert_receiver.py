from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("🚨 ALERT RECEIVED 🚨")
    print(json.dumps(data, indent=2))
    return '', 200

if __name__ == '__main__':
    app.run(port=5001)
