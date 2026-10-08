import random


class egenskaper:
    def __init__(self, hp, dmg, level, namn):
        self.hp = hp
        self.dmg = dmg
        self.level = level
        self.namn = namn

    def print(self):
        return (f"{self.hp}, {self.dmg}, {self.level}, {self.namn}")





spelare = egenskaper(10, 3, 3, "dinmamma")

print("HP", spelare.hp)
print("DMG", spelare.dmg)
print("LEVEL", spelare.level)
print("NAMN", spelare.namn)


zombie = egenskaper(2, 7, 3, "soiehef")

print("HP", zombie.hp)
print("DMG", zombie.dmg)
print("LEVEL", zombie.level)
print("NAMN", zombie.namn)

spöke = egenskaper(4, 3, 2, "oihweg")

print("HP", spöke.hp)
print("DMG", spöke.dmg)
print("LEVEL", spöke.level)
print("NAMN", spöke.namn)


while spelare.hp and zombie.hp and spöke.hp > 0:

    spelare.hp = spelare.hp - zombie.dmg


    if spelare.hp <= 0:
        print("du dog ts")
        print(spelare.hp)
        break
        















