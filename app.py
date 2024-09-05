# A API deverá fornecer dois endpoints:

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import sqlite3
from rpa import pesquisa_clima


app = Flask(__name__)
api = Api(
    app, 
    version='1.0', 
    title='Teste Técnico',
    description='Desenvolvimento de API com Integração de RPA'
)


# banco de dados
def create_db():
    conn = sqlite3.connect('clima.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS clima (
                       id INTEGER PRIMARY KEY, 
                       temperatura TEXT,
                       descricao TEXT,
                       dia TEXT,
                       hora TEXT, 
                       data DATE)
                ''')
    conn.commit()
    conn.close()
    
create_db()


#  model
model_clima = api.model('Clima', {
    'temperatura': fields.String(required=True, description='temperatura', default='42 C'),
    'descricao': fields.String(required=True, description='descricao', default='Sol'),
    'dia': fields.String(required=True, description='dia', default='segunda-feira'),
    'hora': fields.String(required=True, description='hora', default='12:00'),
    'data': fields.String(required=True, description='data', default='01/12/2024')
})


# [GET] /rpa: Endpoint que executa o RPA e retorna os dados extraídos.
@api.route('/rpa')
class RPA(Resource):
    def get(self):
        pesquisa_clima()
        return {'message': 'RPA executado.'}, 200
    

# [POST] /store-data: Endpoint que recebe os dados extraídos pelo RPA e os armazena no banco de dados.
@api.route('/store-data')
class StoreData(Resource):
    @api.expect(model_clima)
    def post(self):
        data = request.json
        conn = sqlite3.connect('clima.db')
        cursor = conn.cursor()
        cursor.execute('''
                    INSERT INTO clima (temperatura, descricao, dia, hora, data) 
                    VALUES (?, ?, ?, ?, ?)
                    ''', (data['temperatura'], data['descricao'], data['dia'], data['hora'], data['data']))
        conn.commit()
        conn.close()
        return {'message': 'Dados armazenados.'}, 201


# [GET] /list-data: Endpoint que retorna os dados armazenados no banco de dados.
@api.route('/list-data')
class ListData(Resource):
    def get(self):
        conn = sqlite3.connect('clima.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clima')
        data = cursor.fetchall()
        conn.close()
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)