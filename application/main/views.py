from flask_restful import Resource, reqparse
from application import api

parser = reqparse.RequestParser()

class DefaultEndpoint(Resource):
    def get(self):
        return {'error': 'Not logged in'}

class Register(Resource):
    pass

class Login(Resource):
    pass

class Upload(Resource):
    def post(self):
        args = parser.parse_args()
        file = args['analyse']
        return {'status': 'Success'}, 201


class Analysis(Resource):
    pass


api.add_resource(DefaultEndpoint, '/')
