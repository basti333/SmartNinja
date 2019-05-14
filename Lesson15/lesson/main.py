from flask import Flask, render_template

app = Flask(__name__)       #erzeugt ein neues Flask app object

@app.route("/")                   #Das ist der Controller, "/" ist die Homepage
def index():
    return render_template("index.html")

@app.route("/impressum")        #wenn die URL geändert wird, ändert sich die Funktion und ein anderes HTML wird aufgerufen
def impressum():
    return render_template("impressum.html")

if __name__ == '__main__':    #if Abfrage, ob es sich hier um die Hauptdatei handelt
    app.run()

