# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
    def heal(self):
        self.health += 10

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    
    def special_ability(self, opponent):
        print("\n--- Select a special ability ---")
        print("1. Crippling Strike")
        print("2. Battle Rage")

        choice = input("Choose a special ability: ")
        
        if choice == '1':
            self.crippling_strike(opponent)
        elif choice == '2':
            self.battle_rage()
        else:
            print("Invalid selection. Defaulting to Crippling Strike.")
            self.crippling_strike(opponent)
            
    def crippling_strike(self, opponent):
        opponent.health -= 20
        opponent.attack_power -= 2
        if opponent.attack_power <= 5:
            opponent.attack_power = 5
        print(f'Crippling Strike was used on {opponent.name}. Their health was reduced to {opponent.health} and attack power to {opponent.attack_power}')

    def battle_rage(self):
        self.health += 5
        self.attack_power += 5
        if self.attack_power > 40:
            self.attack_power = 40
        print(f'{self.name} uses Battle Rage. Their health and attack power were raise by 5. HP: {self.health} AP: {self.attack_power}')

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class

# Create Paladin class 

class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=12)
        
    def special_ability(self, opponent):
        print("\n--- Select a special ability ---")
        print("1. Summon Zombie")
        print("2. Bone Armor")
        
        choice = input("Choose a special ability: ")
        
        if choice == '1':
            print(f'{self.name} summons a zombie. The zombie charges!!')
            opponent.health -= 30
            print(f'Zombie does 30 damage to {opponent.name}. Health reduced to {opponent.health}')
        elif choice == '2':
            self.max_health = 175
            self.health += 40
            if self.health >= self.max_health:
                self.health = self.max_health
            print(f"Bone armor was added. {self.name} has gained 40 health and the max health has increased to {self.max_health}. Health: {self.health}")
        else:
            print("Invalid Selection. Defaulting to Summon Zombie")
            print(f'{self.name} summons a zombie. The zombie charges!!')
            opponent.health -= 30
            print(f'Zombie does 30 damage to {opponent.name}. Health reduced to {opponent.health}')
