# A API deverá fornecer dois endpoints:

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import sqlite3
# from rpa import pesquisa_clima


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
    'temperatura': fields.String(required=True, description='temperatura'),
    'descricao': fields.String(required=True, description='descricao'),
    'dia': fields.String(required=True, description='dia'),
    'hora': fields.String(required=True, description='hora'),
    'data': fields.String(required=True, description='data')
})


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