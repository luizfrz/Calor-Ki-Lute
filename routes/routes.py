from flask import Flask, render_template
app = Flask(_name_)
@app.route("/")
def homepage():
    return render_template("link pagina")
@app.route("/sucess")
def sucess():
    return render_template("link pagina")
@app.route("/erro")
def erro():
    return render_template("link pagina")

if _name_ == "_main_"
@app.run()