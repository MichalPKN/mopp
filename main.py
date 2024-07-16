from flask import Flask, redirect, render_template, request
import sys
from config import api_key, continent, region, riot_id, tag_line
# sys.path is a list of absolute path strings
from components.data_loader import DataLoader
from components.data_processer import DataProcesser


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
        #error might be in data
        return render_template('index.html', error=f"An error occurred: {e}<br>data might not be present, try refreshing them first", name=name)
    except Exception as e:
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