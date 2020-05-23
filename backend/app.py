from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/first_endpoint')
@cross_origin()
def api():
    return jsonify({'hello' : 'chipino!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
