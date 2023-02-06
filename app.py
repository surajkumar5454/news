import json
from datetime import datetime

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


def populatenewswithdate(topic, datepicked):
    # Your API key
    api_key = '20157af1d27548e38a2925331bf1c2d3'
    response = requests.get('https://newsapi.org/v2/everything?q=' + topic + '&apiKey=' + api_key)
    filteredData = []
    # Get the JSON data from the response
    data = json.loads(response.text)
    for article in data['articles']:
        date_object = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
        new_date_string = date_object.strftime("%Y-%m-%d")
        if datepicked == new_date_string:
            filteredData.append(article)
    print(data)
    return filteredData


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    data = []
    topic = request.form['newsstring']
    datepicked = request.form['datepicker']
    print("date: " + datepicked)
    if datepicked == "":
        data = populatenews(topic)
    else:
        data = populatenewswithdate(topic, datepicked)
    return render_template("result.html", data=data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
