from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def get_movies():
    response = requests.get("https://animechan.vercel.app/api/random")

    data = response.json()
    print(data)
    return render_template ("index.html", data)