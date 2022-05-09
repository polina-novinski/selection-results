from flask import Flask, render_template

app = Flask(__name__)


@app.route("/choice/<nickname>/<int:level>/<float:rating>")
def choice(nickname, level, rating):
    res = {}
    res["nickname"] = nickname
    res["level"] = level
    res["rating"] = rating
    return render_template("index.html", res=res)