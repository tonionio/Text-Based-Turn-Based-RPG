import random


class Enemy:
    def __init__(self, health, stamina, attack_name, attack_damage, hit_chance):
        self.health = health
        self.stamina = stamina
        self.attack_name = attack_name
        self.attack_damage = attack_damage
        self.hit_chance = hit_chance

    def __str__(self):
        return f"{self.__class__.__name__}: Health: {self.health}, Stamina: {self.stamina}, Attack: {self.attack_name} ({self.attack_damage} damage)"

    def attack(self, target):
        hit_chance = random.random()
        if hit_chance > self.hit_chance:
            return self.attack_damage
        else:
            return 0

    def take_damage(self, damage):
        self.health -= damage

class Yeti(Enemy):
    def __init__(self):
        super().__init__(health=120, stamina=60, attack_name="frost_bite", attack_damage=18, hit_chance=0.6)


class Mothman(Enemy):
    def __init__(self):
        super().__init__(health=90, stamina=70, attack_name="wing_slap", attack_damage=15, hit_chance=0.7)


class Sandman(Enemy):
    def __init__(self):
        super().__init__(health=100, stamina=80, attack_name="sand_blast", attack_damage=17, hit_chance=0.65)
