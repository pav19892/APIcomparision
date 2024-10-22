from flask import Flask, jsonify

app = Flask(__name__)

# Small data load
@app.route('/small', methods=['GET'])
def small():
    return jsonify(message="This is a small payload", data=[1, 2, 3])

# Medium data load
@app.route('/medium', methods=['GET'])
def medium():
    medium_data = [{"id": _, "name": "John Doe"} for _ in range(100)]
    return jsonify(message="This is a medium payload", data=medium_data)

# Heavy data load
@app.route('/heavy', methods=['GET'])
def heavy():
    heavy_data = [{"id": _, "name": "John Doe","username":f"john{_}"} for _ in range(100000)]
    return jsonify(message="This is a heavy payload", data=heavy_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8013,debug=True)
