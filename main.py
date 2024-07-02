from flask import Flask, redirect, render_template
import sys
# sys.path is a list of absolute path strings
from components.data_loader import DataLoader

continent = "europe"
region = "eun1"
riot_id = "Miapp"
tag_line = "bread"
api_key = "RGAPI-1b5bb1d7-b7a0-44ff-b9a5-bce8805d818b"
n_matches = 10

kesha, Miapp, Standa = True, False, False

if kesha:
    region = "euw1"
    riot_id = "erectwillump"
    tag_line = "boing"
if Miapp:
    region = "eun1"
    riot_id = "Miapp"
    tag_line = "bread"
if Standa:
    region = "eun1"
    riot_id = "Stenly03"
    tag_line = "eune"


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/button-pressed', methods=['POST'])
def button_pressed():
    data_loader = DataLoader(api_key)
    puuid = data_loader.get_puuid(continent, riot_id, tag_line)
    print("loading data")
    data_loader.load_data(puuid, region)
    print("data loaded")
    return "you shouldn't be here"

if __name__ == '__main__':
    app.run(debug=True)