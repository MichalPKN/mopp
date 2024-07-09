from flask import Flask, redirect, render_template, request
import sys
# sys.path is a list of absolute path strings
from components.data_loader import DataLoader
from components.data_processer import DataProcesser

continent = "europe"
region = "eun1"
riot_id = "Miapp"
tag_line = "bread"
api_key = "RGAPI-44899aac-c6f6-41c7-9907-015ca69df0ba"
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

@app.route('/', methods=['GET'])
def main_app():
    data = request.args
    if "stat-request" not in data:
        return render_template('index.html')
    dp = DataProcesser()
    data_loader = DataLoader(api_key)
    puuid = data_loader.get_puuid(continent, riot_id, tag_line)
    name = riot_id + "#" + tag_line
    if name == "erectwillump#boing":
        name = "Kesha"
    try:
        results = dp.process_data(data["stat-request"], puuid)
        return render_template('index.html', stat=data["stat-request"], name=name, results = results)
    except ValueError as e:
        return render_template('index.html', error=f"Invalid stat: {e}", name=name)
    except IndexError as e:
        #raise e
        #error might be in data
        return render_template('index.html', error=f"An error occurred: {e}<br>data might not be present, try refreshing them first", name=name)
    except Exception as e:
        raise e
        return render_template('index.html', error=f"An error occurred: {e}", name=name)
    

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