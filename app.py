import json
import os
from flask import Flask
from flask import request, jsonify
#from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

class TodoList(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('editor1')
        args = parser.parse_args()
        data = args['editor1']
        print(type(data))
        print(data)
        return {"data" : data}

api.add_resource(TodoList, '/')
if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(debug=False, port=port, host='0.0.0.0')
