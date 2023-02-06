import json

import requests
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'  # Replace with a secret key of your own



def populatenews(topic):
    # Your API key
    api_key = '20157af1d27548e38a2925331bf1c2d3'
    response = requests.get('https://newsapi.org/v2/everything?q=' + topic + '&apiKey=' + api_key)

    # Get the JSON data from the response
    data = json.loads(response.text)
    print(data)
    return data["articles"]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    data = []
    topic = request.form['newsstring']
    data = populatenews(topic)
    return render_template("result.html", data=data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
