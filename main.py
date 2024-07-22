from flask import Flask, redirect, render_template, request, jsonify
import sys
from config import continent, region, riot_id, tag_line, puuid
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
    try:
        data = request.get_json()
        api_key = data["API_key"]
        data_loader = DataLoader(api_key)
        puuid_tenp = data_loader.get_puuid(continent, riot_id, tag_line)
        print("loading data")
        n_matches = data_loader.load_data(puuid_tenp, region)
        print("data loaded")
        return jsonify({"message": "Loaded " + str(n_matches) + " matches in"}), 200
    except Exception as e:
        if "403 Client Error: Forbidden for url:" in str(e):
            return jsonify({"error": "Invalid API key"}), 403
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)