import random

hero = {"hp": 30, "attacks": {"bat": 5, "bad_dancing": 100}, "armor_class": 10}


class Attack:
    def __init__(self, name, dice, plus_to_hit, plus_for_damage, uses_per_round):
        self.name = name
        self.dice = dice
        self.plus_to_hit = plus_to_hit
        self.plus_for_damage = plus_for_damage
        self.uses_per_round = uses_per_round


class Combatant:
    'Common base class for all combatants'

    def __init__(self, name, enemy_hero_flag, hit_dice, hit_dice_count, hit_dice_mod, attacks, ac):
        self.name = name
        self.enemy_hero_flag = enemy_hero_flag
        self.attacks = attacks
        self.hit_dice = hit_dice
        self.hit_dice_mod = hit_dice_mod
        self.hit_dice_count = hit_dice_count
        self.ac = ac
        self.hp = gen_hit_points(hit_dice, hit_dice_count, hit_dice_mod)

    def display_combatant(self):
        print
        "Name : ", self.name, ", Type: ", self.type, ", HP", self.hp

    def gen_hit_points(self):
        hp = 0

        for i in range(self.hit_dice_count):
            hp += random.randint(1, self.hit_dice)

        hp = hp + self.hit_dice_mod


def build_dragon():
    dragon = Combatant("Geek1")
    return dragon


def build_heroes():
    pass


def fight(enemies, heroes):
    pass


if __name__ == "__main__":
    print("hello")
    dragon = build_dragon()
    heroes = build_heroes()
    fight(dragon, heroes)
