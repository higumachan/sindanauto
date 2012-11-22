#coding: utf-8

from flask import *
import main
import json
import crawl_sindan

app = Flask(__name__);

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/result", methods=["GET"])
def result():
    return render_template("result.html", name=request.args["name"]);

@app.route("/hot")
def hot():
    result = crawl_sindan.crawl();
    return json.dumps(result);

@app.route("/sindan/<int:id>")
def sindan(id):
    name = request.args["name"];
    result = main.try_sindan(id, name);
    return json.dumps(result);

if __name__ == "__main__":
    app.debug = True;
    app.run();

