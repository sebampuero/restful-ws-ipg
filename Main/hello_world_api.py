from flask import Flask
from flask import request
from flask import Response
from Service.Parser import get_firmen_objects

app = Flask(__name__)


@app.route('/firmen', methods=['GET'])
def get():
    name = request.args.get('name', '')
    branche = request.args.get('branche', '')
    ort = request.args.get('ort', '')
    rolle = request.args.get('rolle', '')
    firmen_list = get_firmen_objects(name,branche,ort,rolle)
    return Response(firmen_list, mimetype="application/json")


if __name__ == "__main__":
    app.run()
