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


@app.route("/test", methods=["GET"])
def test():
    return render_template("test.html");

@app.route("/hot")
def hot():
    if (request.args.has_key("mode")):
        mode = request.args["mode"];
    else:
        mode = "hot";
    result = crawl_sindan.crawl();
    return json.dumps(result);

@app.route("/sindan/<int:id>")
def sindan(id):
    name = request.args["name"];
    result = main.try_sindan(id, name);
    return json.dumps(result);

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")

if __name__ == "__main__":
    app.debug = True;
    app.run();

