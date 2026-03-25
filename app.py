from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask App!'}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'key': 'value'}
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)