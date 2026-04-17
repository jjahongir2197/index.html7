from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def check():

    if request.method == "POST":

        num = int(request.form["num"])

        if num > 0:
            return "Musbat"
        elif num < 0:
            return "Manfiy"
        else:
            return "0"

    return render_template("index.html")

app.run(debug=True)
