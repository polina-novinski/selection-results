from flask import Flask,  render_template

app = Flask(__name__)

@app.route("/training/<prof>", methods=["GET"])
def mars(title):
    if "инженер" in title or "строитель" in title:
        return render_template("ing.html", title=title)
    return render_template("nayk.html", title=title)