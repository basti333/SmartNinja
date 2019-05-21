from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    page_title = "Homepage"
    current_year = datetime.datetime.now().year
    cities = ["Vienna", "Vancouver", "Los Angeles", "Peking"]

    return render_template("index.html", page_title=page_title, current_year=current_year, cities=cities)


@app.route("/about")
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", user_name=user_name)

    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response

if __name__ == '__main__':
    app.debug = True
    app.run()