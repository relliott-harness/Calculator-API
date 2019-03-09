from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_data(data, func_name):
    if func_name == 'add' or func_name == 'subtract' or func_name == 'multiply':
        if len(data) != 2:
            return "ERROR: incorrect number of paramters", 301
        else:
            return "", 200
    elif func_name == 'divide':
        if len(data) != 2:
            return "ERROR: incorrect number of paramters", 301
        elif data['y'] == 0:
            return "ERROR: divide by zero", 302
        else:
            return "", 200


# resource for adding two numbers
# if a request hits the /add endpoint, the api will determine what type of
# request it is
class Add(Resource):
    # when a request comes into the /add endpoint and it is a POST, invoke
    def post(self):
        data = request.get_json()

        msg, status_code = check_data(data,'add')
        if status_code != 200:
            return jsonify({
                'Message': msg,
                'Status Code': status_code
            })

        x = data['x']
        y = data['y']
        sum = x+y
        ret = {
            'Message': sum,
            'Status Code': 200
        }
        return jsonify(ret)

class Subtract(Resource):
    def post(self):
        data = request.get_json()
        msg, status_code = check_data(data, 'subtract')
        if status_code != 200:
            return jsonify({
                'Message': msg,
                'Status Code': status_code
            })

        x = data['x']
        y = data['y']
        diff = x-y
        ret = {
            'Message': diff,
            'Status Code': 200
        }
        return jsonify(ret)

class Multiply(Resource):
    def post(self):
        data = request.get_json()
        msg, status_code = check_data(data, 'multiply')
        if status_code != 200:
            return jsonify({
                'Message': msg,
                'Status Code': status_code
            })

        x = data['x']
        y = data['y']
        prod = x*y
        ret = {
            'Message': prod,
            'Status Code': 200
        }
        return jsonify(ret)

class Divide(Resource):
    def post(self):
        data = request.get_json()
        msg, status_code = check_data(data, 'divide')
        if status_code != 200:
            return jsonify({
                'Message': msg,
                'Status Code': status_code
            })

        x = data['x']
        y = data['y']
        quotient = (x*1.0) / y
        ret = {
            'Message': quotient,
            'Status Code': 200
        }
        return jsonify(ret)

api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')

if __name__ == '__main__':
    app.run()
