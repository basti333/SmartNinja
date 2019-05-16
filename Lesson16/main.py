from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    page_title = "Homepage"
    current_year = datetime.datetime.now().year
    cities = ["Vienna", "Vancouver", "Los Angeles", "Peking"]

    return render_template("index.html", page_title=page_title, current_year=current_year, cities=cities)


@app.route("/about-me")
def about():
    return render_template("about.html", )


if __name__ == '__main__':
    app.run()