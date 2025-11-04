import json


def get_club_with_most_wins(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not data:
            return []

        max_wins = max(club["wins"] for club in data)
        best_clubs = [club for club in data if club["wins"] == max_wins]

        return best_clubs
    except ValueError:
        return "Wrong JSON format or file error"
