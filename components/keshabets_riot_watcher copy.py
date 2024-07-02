from riotwatcher import LolWatcher, RiotWatcher, ApiError
import json

continent = "europe"
region = "eun1"
riot_id = "Miapp"
tag_line = "bread"
api_key = "RGAPI-1b5bb1d7-b7a0-44ff-b9a5-bce8805d818b"
n_matches = 10

kesha, Miapp, Standa = False, True, False

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
    
lol_watcher = LolWatcher(api_key)

riot_watcher = RiotWatcher(api_key)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
#my_ranked_stats = lol_watcher.league.by_summoner(region, summoner['id'])
#print(my_ranked_stats)

# def get_account_puuid(continent, riot_id, tag_line, api_key):
#     url = f"https://{continent}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tag_line}?api_key={api_key}"
#     response = requests.get(url)
#     return response.json().get("puuid")

# def get_champion_mastery(region, puuid, api_key):
#     url = f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={api_key}"
#     print(url) 
#     response = requests.get(url)
#     return response.json()

def get_match_history(summoner, puuid, n_matches=10):
    # url = f"https://{continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={n_matches}&api_key={api_key}"
    # response = requests.get(url)
    wins = 0
    kills = 0
    assists = 0
    test = False
    try:
        matches = lol_watcher.match.matchlist_by_puuid(region, puuid, 0, n_matches)
        for match_id in matches:
            match = lol_watcher.match.by_id(region, match_id)
            if test:
                # Convert match data to JSON
                match_data = json.dumps(match)
                # Write JSON to HTML file
                with open("match_data.html", "w") as file:
                    file.write(match_data)
                test = False
            if match.get("info").get("participants")[0].get("win"):
                wins += 1
            kills += match.get("info").get("participants")[0].get("kills")
            assists += match.get("info").get("participants")[0].get("assists")
            print(f"Match {match_id} - {match.get('info').get('participants')[0].get('win')}")
        kd = kills/n_matches
        return wins/n_matches, kd
    except ApiError as err:
        if err.response.status_code == 404:
            print("No matches found")
            return
        else:
            print("something went wrong")
            raise
    

def main_app(params=None):
    account = riot_watcher.account.by_riot_id(continent, riot_id, tag_line)
    summoner = lol_watcher.summoner.by_puuid(region, account['puuid'])
    print(summoner)
    puuid = summoner['puuid']
    #get_match_history(summoner, puuid, n_matches)
    winrate, kd = get_match_history(summoner, puuid, n_matches)
    print(f"---------- {riot_id}#{tag_line} ---------\n")
    print(f"Winrate(last {n_matches} matches): {winrate*100:.2f}%")
    print(f"K/D ratio(last {n_matches} matches): {kd:.2f}")
    print("\n------------------")
    return "Done"
    
if __name__ == "__main__":
    main_app()
