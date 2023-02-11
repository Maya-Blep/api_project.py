from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/quote")
def get_quotes():
    response = requests.get("https://animechan.vercel.app/api/random")
    data = response.json()
    #data = {'anime': 'Avatar: The Last Airbender', 'character': 'Toph Bei Fong', 'quote': "Somebody's a little light on his feet. What's your fighting name, the Fancy Dancer?"}
    print(data)
    return render_template ("quote.html", data = data)



if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')


#<img src= "https://i.pinimg.com/originals/05/bc/84/05bc8496dfae86b4bcb185204591f4fc.jpg">
