from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

app = Flask(__name__, 
    static_url_path='',
    static_folder='.'
)

CORS(app)

from graphs import summary_graph

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Covid19 Cuba API GRAPH'
    })

@app.route('/summary', methods=['POST'])
def summary():
    
    filename = summary_graph(request.json)

    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)