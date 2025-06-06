import json

def load_match_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

    

def win_loss_ratio(matches):
    wins=sum(1 for match in matches if match['result']== 'win')
    losses = sum(1 for match in matches if match['result']=='loss')
    return wins,losses

def top_rum_scorer(matches):
    return max(matches, key=lambda x: x['top_scorer_runs'])['top_scorer']
