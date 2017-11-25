from flask import Flask
from flask import request
from flask import Response
from Service.Parser import get_firmen_JSON
from Config.format import format,post_string,pre_string

app = Flask(__name__)


@app.route('/firmen', methods=['GET'])
def get():
    name = request.args.get('name', '').lower()
    branche = request.args.get('branche', '').lower()
    ort = request.args.get('ort', '').lower()
    rolle = request.args.get('rolle', '').lower()
    print(rolle)
    if name == "" and branche == "" and ort == "" and rolle == "":
        return Response("Keine Parameter wurden eingegeben", status=400,mimetype="text/html")
    firmen_list = get_firmen_JSON(name, branche, ort, rolle)
    return Response(pre_string+firmen_list+post_string, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run()
