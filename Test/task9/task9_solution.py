import random


class Hero:
    def __init__(self, hero_id, team):
        self.hero_id = hero_id
        self.team = team
        self.level = 1

    def level_up(self):
        self.level += 1
        return self.level


class Soldier:
    def __init__(self, soldier_id, team):
        self.soldier_id = soldier_id
        self.team = team

    def move_to_hero(self, hero):
        return f"Солдат {self.soldier_id} следует за героем {hero.hero_id}"


def game_case():
    hero1 = Hero(hero_id=1, team="Red")
    hero2 = Hero(hero_id=2, team="White")

    soldiers = [Soldier(i, random.choice(["Red", "White"])) for i in range(10)]

    red_team = [s for s in soldiers if s.team == "Red"]
    white_team = [s for s in soldiers if s.team == "Blue"]

    if len(red_team) > len(white_team):
        hero1.level_up()
        winner = hero1
    elif len(white_team) > len(red_team):
        hero2.level_up()
        winner = hero2
    else:
        winner = None

    soldier_to_follow = random.choice(red_team)
    soldier_to_follow.move_to_hero(hero1)

    print(f"Hero: {hero1.hero_id}")
    print(f"Soldier: {soldier_to_follow.soldier_id}")


random.seed(0)
result = game_case()


assert isinstance(result["hero1_level"], int)
assert isinstance(result["hero2_level"], int)
assert result["winner_team"] in ["Red", "White", "Ничья"]
assert "следует за героем" in result["follow_info"]
