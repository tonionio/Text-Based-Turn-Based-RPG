import random


class Character:
    def __init__(self, health, max_health, stamina, max_stamina, actions, attack_name, attack_damage, block_name, block_reduction, block_power, hit_chance):
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.health = health
        self.stamina = stamina
        self.actions = actions
        self.attack_name = attack_name
        self.attack_damage = attack_damage
        self.block_name = block_name
        self.block_reduction = block_reduction
        self.blocking_power = block_power
        self.hit_chance = hit_chance

    def __str__(self):
        return f"{self.__class__.__name__}: Health: {self.health}, Stamina: {self.stamina}, Actions: {', '.join(self.actions)}, Attack: {self.attack_name} ({self.attack_damage} damage), Block: {self.block_name} ({self.block_reduction} damage reduction)"

    def attack(self, enemy):
        hit_chance = random.random()  # Generates a random float between 0 and 1
        if hit_chance > self.hit_chance:
            enemy.take_damage(self.attack_damage)
            return self.attack_damage
        else:
            return 0

    def take_damage(self, damage):
        self.health -= damage

    def block(self, enemy):
        incoming_damage = enemy.attack(self)
        blocked_damage = int(incoming_damage * 0.75)
        actual_damage = max(incoming_damage - blocked_damage, 0)
        self.health -= actual_damage
        return blocked_damage, actual_damage


class Warrior(Character):
    def __init__(self):
        super().__init__(health=100,
                         max_health=100,
                         stamina=50,
                         max_stamina=50,
                         actions=["strike", "block"],
                         attack_name="strike", attack_damage=15,
                         block_name="block", block_reduction=10,
                         hit_chance=0.7,
                         block_power=15)


class Ranger(Character):
    def __init__(self):
        super().__init__(health=80,
                         max_health=80,
                         stamina=70,
                         max_stamina=70, actions=["shoot", "block"],
                         attack_name="shoot", attack_damage=12,
                         block_name="block", block_reduction=8,
                         hit_chance=0.7,
                         block_power=15)


class Wizard(Character):
    def __init__(self):
        super().__init__(health=60,
                         max_health=60,
                         stamina=90, max_stamina=90,
                         actions=["cast spell", "block"],
                         attack_name="cast spell", attack_damage=20,
                         block_name="block",
                         hit_chance=0.6, block_reduction=5,
                         block_power=15)
