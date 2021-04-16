"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1><h2>Demo flask</h2><h3>by JoanMBQ</h3>"

@app.route('/suma')
def suma():
    resultado = 523 + 4234
    return "<h3>523 + 4234 = %d</h3>" % (resultado)

@app.route('/listado')
def listado():
    return  "<h2>Listado de materias del itinerario basado en plataformas</h2><ul></ul><li>Plataformas Web</li><li>Plataformas Moviles</li><li>Plataformas para Juegos</li></ul>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
