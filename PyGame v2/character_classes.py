import random

class Character():
    def __init__(self, character_description="", health=0, max_health=0, stamina=0, max_stamina=0, actions=None, attack_name="", attack_damage=0, block_name="", block_reduction=0, hit_chance=0, block_power=0, special_attack_name="", special_attack_damage=0):
        if actions is None:
            actions = [" ", ""]
        self.character_description = character_description
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.actions = actions
        self.attack_name = attack_name
        self.attack_damage = attack_damage
        self.block_name = block_name
        self.block_reduction = block_reduction
        self.hit_chance = hit_chance
        self.block_power = block_power
        self.special_attack_name = special_attack_name
        self.special_attack_damage = special_attack_damage

    def attack(self, enemy):
        hit_chance = random.random()  # Generates a random float between 0 and 1
        if hit_chance > self.hit_chance:
            enemy.take_damage(self.attack_damage)
            return self.attack_damage
        else:
            return 0

    def special_attack(self, enemy):
        if self.stamina >= 20:
            self.stamina -= 20
            enemy.take_damage(self.special_attack_damage)
            return self.special_attack_damage
        elif self.stamina < 20:
            print("You don't have enough stamina to use this attack.")
            return 0
            

    def take_damage(self, damage):
        self.health -= damage

    def block(self, enemy):
        incoming_damage = enemy.attack(self)
        blocked_damage = int(incoming_damage * 0.75)
        actual_damage = max(incoming_damage - blocked_damage, 0)
        self.health -= actual_damage
        return blocked_damage, actual_damage
    
    def to_dict(self):
        return {
            "character_description": self.character_description,
            "health": self.health,
            "max_health": self.max_health,
            "stamina": self.stamina,
            "max_stamina": self.max_stamina,
            "actions": self.actions,
            "attack_name": self.attack_name,
            "attack_damage": self.attack_damage,
            "block_name": self.block_name,
            "block_reduction": self.block_reduction,
            "hit_chance": self.hit_chance,
            "block_power": self.block_power,
            "special_attack_name": self.special_attack_name,
            "special_attack_damage": self.special_attack_damage
        }


    def __str__(self):
        return (f"{self.__class__.__name__} - {self.character_description}\n"
            f"   Health: {self.health}/{self.max_health}\n"
            f"   Stamina: {self.stamina}/{self.max_stamina}\n"
            f"   Attack: {self.attack_name} ({self.attack_damage} damage)\n"
            f"   Block: {self.block_name} ({self.block_reduction} damage reduction)\n"
            f"   Special: {self.special_attack_name} ({self.special_attack_damage} damage)")

class Warrior(Character):
    def __init__(self, additional_attributes = None):
        super().__init__(character_description="A strong and hardy warrior with a powerful sword.",
                         health=100,
                         max_health=100,
                         stamina=50,
                         max_stamina=50,
                         actions=["strike", "block"],
                         attack_name="strike", attack_damage=15,
                         block_name="block", block_reduction=10,
                         hit_chance=0.75,
                         block_power=15, 
                         special_attack_name="charge", 
                         special_attack_damage=30)
        self.additional_attributes = additional_attributes

    def to_dict(self):
        data = super().to_dict()
        data.update(self.additional_attributes)
        return data
        
    def __str__(self):
        return (f"{self.__class__.__name__} - {self.character_description}\n"
            f"   Health: {self.health}/{self.max_health}\n"
            f"   Stamina: {self.stamina}/{self.max_stamina}\n"
            f"   Attack: {self.attack_name} ({self.attack_damage} damage)\n"
            f"   Block: {self.block_name} ({self.block_reduction} damage reduction)\n"
            f"   Special: {self.special_attack_name} ({self.special_attack_damage} damage)")
    
    

               
class Ranger(Character):
    def __init__(self, additional_attributes = None):
        super().__init__(character_description="A skilled ranger with a deadly bow.",
                         health=80,
                         max_health=80,
                         stamina=70,
                         max_stamina=70, actions=["shoot", "block"],
                         attack_name="shoot", attack_damage=12,
                         block_name="block", block_reduction=8,
                         hit_chance=0.75,
                         block_power=15, 
                         special_attack_name="snipe",
                         special_attack_damage=25)
        self.additional_attributes = additional_attributes

    def to_dict(self):
        data = super().to_dict()
        data.update(self.additional_attributes)
        return data
        
    def __str__(self):
        return (f"{self.__class__.__name__} - {self.character_description}\n"
            f"   Health: {self.health}/{self.max_health}\n"
            f"   Stamina: {self.stamina}/{self.max_stamina}\n"
            f"   Attack: {self.attack_name} ({self.attack_damage} damage)\n"
            f"   Block: {self.block_name} ({self.block_reduction} damage reduction)\n"
            f"   Special: {self.special_attack_name} ({self.special_attack_damage} damage)")



class Wizard(Character):
    def __init__(self, additional_attributes = None):
        super().__init__(character_description="A wise wizard with a powerful staff.",
                         health=60,
                         max_health=60,
                         stamina=90, max_stamina=90,
                         actions=["cast spell", "block"],
                         attack_name="cast spell", attack_damage=20,
                         block_name="block",
                         hit_chance=0.75, block_reduction=5,
                         block_power=15,
                         special_attack_name="fireball",
                         special_attack_damage=35)
        self.additional_attributes = additional_attributes

    def to_dict(self):
        data = super().to_dict()
        data.update(self.additional_attributes)
        return data
        
    def __str__(self):
        return (f"{self.__class__.__name__} - {self.character_description}\n"
            f"   Health: {self.health}/{self.max_health}\n"
            f"   Stamina: {self.stamina}/{self.max_stamina}\n"
            f"   Attack: {self.attack_name} ({self.attack_damage} damage)\n"
            f"   Block: {self.block_name} ({self.block_reduction} damage reduction)\n"
            f"   Special: {self.special_attack_name} ({self.special_attack_damage} damage)")

