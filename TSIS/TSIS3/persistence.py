import json

def load_leaderboard():
    try:
        with open("leaderboard.json") as f:
            return json.load(f)
    except:
        return []

def save_leaderboard(data):
    with open("leaderboard.json", "w") as f:
        json.dump(data, f, indent=4)

def add_score(name, score):
    data = load_leaderboard()
    data.append({"name": name, "score": score})
    data = sorted(data, key=lambda x: x["score"], reverse=True)
    save_leaderboard(data[:5])

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"selected_car": 0}

def save_settings(selected):
    with open("settings.json", "w") as f:
        json.dump({"selected_car": selected}, f)