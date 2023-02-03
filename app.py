from flask import Flask, request

# Cria a instância Flask
app = Flask(__name__)

# Define uma rota que retorna o nome da pessoa
# passada como parâmetro na URL
@app.route('/hello/<name>')
def hello(name):
    return f"Olá, {name}!"

# Define uma rota que soma dois números passados
# como parâmetros na URL
@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    return str(a + b)