import random


class egenskaper:
    def __init__(self, hp, dmg, level, namn, attack):
        self.hp = hp
        self.dmg = dmg
        self.__level = level
        self.namn = namn
        self.attack = attack


    def get_level(self):
        return self.__level

    def print(self):
        return (f"{self.hp}, {self.dmg}, {self.level}, {self.namn}")



class spelare(egenskaper):
    def attack(self, attack):
        print(f"Du attakerar med {self.attack}")




#class attack(egenskaper):
    def attack(self, attack, dmg, hp):
        print(f"Attack med {self.attack} och gör {self.dmg} skada")







s1 = spelare(10, 3, 3, "dinmamma", "FIREBALL")

print("HP", s1.hp)
print("DMG", s1.dmg)
print("LEVEL", s1.get_level())
print("NAMN", s1.namn)

print('')


zombie = egenskaper(2, 7, 3, "soiehef", "BITER")


print("HP", zombie.hp)
print("DMG", zombie.dmg)
print("LEVEL", zombie.get_level())
print("NAMN", zombie.namn)

print('')

spöke = egenskaper(4, 3, 2, "oihweg", "SKUMMYT SPÖK SLIME")

print("HP", spöke.hp)
print("DMG", spöke.dmg)
print("LEVEL", spöke.get_level())
print("NAMN", spöke.namn)

print('')



while s1.hp and zombie.hp and spöke.hp > 0:

    s1.hp = s1.hp - zombie.dmg

    s1.attack(spelare.attack)

    print(s1.hp)


    if s1.hp <= 0:
        print("du dog ts")
        print(s1.hp)
        break
    
        















