import random

class monster:
    def __init__(self, name, hp, level, dmg, attack):
        self.name = name
        self.hp = hp
        self.__level = level
        self.attack = attack
        self.dmg = dmg

    def get_level(self):
        return self.__level

    def mattack(self):
        return(f"{self.name} attackerar med {self.attack} och gör {self.dmg} skada!")



class Zombie(monster):
    def __init__(self):
        super().__init__("ZOMBIE", 30, 2, 4, "KLÖSER")

class Spöke(monster):
    def __init__(self):
        super().__init__("SPÖKE", 60, 3, 6, "SPOTT!?")


class spelare:
    def __init__(self, hp, level, attack, dmg):
        self.hp = hp
        self.__level = level
        self.attack = attack
        self.dmg = dmg
        
    def get_level(self):
        return self.__level

    
    def sattack(self):
        print(f"du attackerar med {self.attack} och gör {self.dmg} skada.")

dawgs = [Spöke(), Zombie()]


Du = spelare(70, 5, "FIREBALL", 10)


spelare_name = input("vad heter du?   ")
print(f"nej men fantastiskt {spelare_name}, är du redo att slåss? ps. du har inget val")



current_monster = random.choice(dawgs)

print(current_monster)

while Du.hp or current_monster.hp > 0:

 

    Du.hp = Du.hp - current_monster.dmg

    print(f"{current_monster.name} attackerar med {current_monster.attack}")
    print(f"D tog {current_monster.dmg} och har {Du.hp} hp kvar")
    print("Dags att slå tillbaka!")


    print(f"DU attackerar med {Du.attack} och gör {Du.dmg}")    

    current_monster.hp = current_monster.hp - Du.dmg

    print(f"{current_monster.name} har {current_monster.hp} HP kvar!")

    
    if Du.hp <= 0:
        print("du dog ts")
        print(Du.hp)
        break

    elif current_monster.hp <=0:
        print("Monstret dog! Du gjorde de!")
        break
    




