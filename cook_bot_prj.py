from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
app.secret_key = 'alex'


class Item(Resource):
    def write_json(data, filename='answer.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def post(self):
        data = request.get_json(force=True)
        self.write_json(data)
        return jsonify(data)


api.add_resource(Item, '/')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
