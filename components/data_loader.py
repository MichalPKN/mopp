from riotwatcher import LolWatcher, RiotWatcher, ApiError
import json
    
class DataLoader:
    def __init__(self, api_key):
        self.lol_watcher = LolWatcher(api_key)
        self.riot_watcher = RiotWatcher(api_key)
        
    def get_puuid(self, continent, riot_id, tag_line):
        try:
            account = self.riot_watcher.account.by_riot_id(continent, riot_id, tag_line)
            return account["puuid"]
        except ApiError as err:
            raise
    
    def load_data(self, puuid, region):
        lol_watcher = self.lol_watcher
        n_matches = 100
        try:
            matches = lol_watcher.match.matchlist_by_puuid(region, puuid, 0, n_matches)
            with open("match_stats.json", "r+") as file:
                match_json = json.load(file)
                exists = False
                for user in match_json:
                    if user["puuid"] == puuid:
                        user["match_ids"] = matches
                        exists = True
                        summoner_i = match_json.index(user)
                        summoner = user
                        break
                if not exists:
                    summoner = {"puuid": puuid, "last_match": "", "matches": []}
                    match_json.append(summoner)
                    summoner_i = len(match_json) - 1
                for match_id in matches:
                    if match_id == summoner["last_match"]:
                        break
                    match = lol_watcher.match.by_id(region, match_id)
                    match_json[summoner_i]["matches"].append(match)
                match_json[summoner_i]["last_match"] = matches[0]
                file.seek(0)
                file.truncate()
                json.dump(match_json, file)
                return
        except ApiError as err:
            raise
        
    