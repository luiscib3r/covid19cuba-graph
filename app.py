from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

app = Flask(__name__, 
    static_url_path='',
    static_folder='.'
)

CORS(app)

from graphs import summary_graph, evolution_graph
from graphs import evolution_recuperados_graph
from graphs import evolution_fallecidos_graph 
from graphs import sexo_graph, modo_graph, pais_graph
from graphs import nacionalidad_graph, edad_graph, tests_graph, provincias_graph, municipios_graph

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Covid19 Cuba API GRAPH'
    })

@app.route('/summary', methods=['POST'])
def summary():
    
    filename = summary_graph(request.json)

    return send_file(filename)

@app.route('/evolution', methods=['POST'])
def evolution():

    filename = evolution_graph(request.json)

    return send_file(filename)

@app.route('/evolution_recuperados', methods=['POST'])
def evolution_recuperados():

    filename = evolution_recuperados_graph(request.json)

    return send_file(filename)

@app.route('/evolution_fallecidos', methods=['POST'])
def evolution_fallecidos():

    filename = evolution_fallecidos_graph(request.json)

    return send_file(filename)

@app.route('/sexo', methods=['POST'])
def sexo():

    filename = sexo_graph(request.json)

    return send_file(filename)

@app.route('/modo', methods=['POST'])
def modo():

    filename = modo_graph(request.json)

    return send_file(filename)

@app.route('/pais', methods=['POST'])
def pais():

    filename = pais_graph(request.json)

    return send_file(filename)

@app.route('/nacionalidad', methods=['POST'])
def nacionalidad():

    filename = nacionalidad_graph(request.json)

    return send_file(filename)

@app.route('/edad', methods=['POST'])
def edad():

    filename = edad_graph(request.json)

    return send_file(filename)

@app.route('/tests', methods=['POST'])
def tests():

    filename = tests_graph(request.json)

    return send_file(filename)

@app.route('/provincias', methods=['POST'])
def provincias():

    filename = provincias_graph(request.json)

    return send_file(filename)

@app.route('/municipios', methods=['POST'])
def municipios():

    filename = municipios_graph(request.json)

    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)