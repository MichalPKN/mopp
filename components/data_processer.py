import json
import re

class DataProcesser:
    def __init__(self):
        pass

    def process_data(self, query, puuid, indexes=[5, 10]):
        with open('match_stats.json', 'r') as file:
            data = json.load(file)
            i_matches = 0
            results = []
            vals = 0
            for word in self.split_words(query):
                if not word.isdigit() and word != "darkHarvestStacks" and word not in data[0]["matches"][0]["info"]["participants"][0]:
                    raise ValueError(word)
            for user in data:
                if user["puuid"] == puuid:
                    for match in user["matches"]:
                        for participant in match["info"]["participants"]:
                            if participant["puuid"] == puuid:
                                if "darkHarvestStacks" in query and participant["darkHarvestStacks"] == "N/A":
                                    continue
                                #print(participant["darkHarvestStacks"])
                                vals += 1 if eval(query, {}, participant) else 0
                                i_matches += 1
                                if i_matches in indexes:
                                    results.append([i_matches, vals/i_matches*100])
            results.append([i_matches, vals/i_matches*100])
        return results
    
    def split_words(self, query):
        return re.findall(r"[\w.]+", query)
    
    