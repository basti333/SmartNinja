from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def solution():
    num_1 = float(request.form.get("num_1"))
    operation = request.form.get("operation")
    num_2 = float(request.form.get("num_2"))

    if operation == "+":
        solution = (num_1 + num_2)
        response = make_response(render_template("index.html", solution=solution))
        return response
    elif operation == "-":
        solution = (num_1 - num_2)
        response = make_response(render_template("index.html", solution=solution))
        return response
    elif operation == "*":
        solution = (num_1 * num_2)
        response = make_response(render_template("index.html", solution=solution))
        return response
    elif operation == "/":
        solution = (num_1 / num_2)
        response = make_response(render_template("index.html", solution=solution))
        return response
    else:
        solution = "Bei der Eingabe ist etwas schief gelaufen. Bitte versuche es erneut."
        response = make_response(render_template("index.html", solution=solution))
        return response

if __name__ == "__main__":
    app.run()

