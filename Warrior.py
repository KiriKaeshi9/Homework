import random


class Warrior:
    damage = 20

    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def battle(self, self1):
        while self.hp > 0 and self1.hp > 0:
            if random.randint(1, 2) == 1:
                self.hp -= self.damage
                print(self1.name, 'hits', self.name + ', warrior', self.name, 'has left', self.hp, 'heal points.')
            else:
                self1.hp -= self.damage
                print(self.name, 'hits', self1.name + ', warrior', self1.name, 'has left', self1.hp, 'heal points.')
        if self.hp > self1.hp:
            print('Warrior', self.name, 'won the battle.')
        else:
            print('Warrior', self1.name, 'won the battle.')


viking = Warrior('Viking')
samurai = Warrior('Samurai')
Warrior.battle(samurai, viking)

