from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    query = "London,uk"
    unit = "metric"
    api_key = "025bc28c3628942255420505a79793cc"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(query, unit, api_key)
    data = requests.get(url=url)
    return render_template("index.html", data=data.json())



if __name__ == '__main__':
    app.run()