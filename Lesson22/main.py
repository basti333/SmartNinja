import random
import uuid
import hashlib
from flask import Flask, render_template, request, make_response, redirect, url_for
from Lesson22.models import User

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    session_token = request.cookies.get("session_token")

    if session_token:
        user = User.fetch_one(query=["session_token", "==", session_token])
    else:
        user = None

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    password = request.form.get("user-password")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # create a secret number
    secret_number = random.randint(1, 30)

    # see if user already exists
    user = User.fetch_one(query=["email", "==", email])

    if not user:
        # create a User object
        user = User(name=name, email=email, password=hashed_password, secret_number=secret_number)
        user.create()  # save the object into a database

    if hashed_password != user.password:
        return "Wrong Password! Go back and try again."
    elif hashed_password == user.password:
        session_token = str(uuid.uuid4())    #neuer session token wird erstellt
        User.edit(obj_id=user.id, session_token=session_token)   #session token in datenbank speichern

        #session token wird in den cookie gespeichert statt der E-Mail, DATENSCHUTZ

        response = make_response(redirect(url_for('index')))
        response.set_cookie("session_token", session_token, httponly=True, samesite='Strict')


    return response

@app.route("/logout")
def logout():

    response = make_response(redirect(url_for('index')))
    response.set_cookie("session_token", expires=0)

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))

    session_token = request.cookies.get("session_token")

    # get user from the database based on her/his email address
    user = User.fetch_one(query=["session_token", "==", session_token])

    if guess == user.secret_number:
        message = "Correct! The secret number is {0}".format(str(guess))

        # create a new random secret number
        new_secret = random.randint(1, 30)

        # update the user's secret number in the User collection
        User.edit(obj_id=user.id, secret_number=new_secret)
    elif guess > user.secret_number:
        message = "Your guess is not correct... try something smaller."
    elif guess < user.secret_number:
        message = "Your guess is not correct... try something bigger."

    return render_template("result.html", message=message)

@app.route("/profile", methods=["GET"])
def profile():
    session_token = request.cookies.get("session_token")

    user = User.fetch_one(query=["session_token", "==", session_token])

    if user:
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for("index"))




@app.route("/profile/edit", methods=["GET", "POST"])
def profile_edit():
    session_token = request.cookies.get("session_token")

    user = User.fetch_one(query=["session_token", "==", session_token])

    if request.method == "GET":
        if user:
            return render_template("profile_edit.html", user=user)
        else:
            return redirect(url_for("index"))

    elif request.method == "POST":
        name = request.form.get("profile-name")
        email = request.form.get("profile-email")

        User.edit(obj_id=user.id, name=name, email=email)

        return redirect(url_for("profile"))


@app.route("/profile/delete", methods=["GET", "POST"])
def profile_delete():
    session_token = request.cookies.get("session_token")

    user = User.fetch_one(query=["session_token", "==", session_token])

    if request.method == "GET":
        if user:
            return render_template("profile_delete.html", user=user)
        else:
            return redirect(url_for("index"))

    elif request.method == "POST":
        User.delete(obj_id=user.id)
        return redirect(url_for("index"))

@app.route("/users", methods=["GET"])
def all_users():
    users = User.fetch()

    return render_template("users.html", users=users)

@app.route("/user/<user_id>", methods=["GET"])
def user_details(user_id):
    user = User.get(obj_id=user_id)

    return render_template("user_details.html", user=user)

if __name__ == '__main__':
    app.run()
