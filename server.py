from flask import Flask, request, Response,redirect
from Service.Parser import get_firmen_JSON
from Config.format import post_string,pre_string

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("/firmen")

@app.route('/firmen', methods=['GET'])
def get():
    name = request.args.get('name', '').lower().strip()
    branche = request.args.get('branche', '').lower().strip()
    ort = request.args.get('ort', '').lower().strip()
    rolle = request.args.get('rolle', '').lower().strip()
    if name == "" and branche == "" and ort == "" and rolle == "":
        return Response("<h3>Keine Parameter wurden eingegeben</h3>", status=400,mimetype="text/html")
    firmen_list = get_firmen_JSON(name, branche, ort, rolle)
    return Response(pre_string+firmen_list+post_string, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
