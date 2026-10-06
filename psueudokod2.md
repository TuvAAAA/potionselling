jag lowkirkly orkar inte med kaffeét

intro till dungeon

monster:
    zombie
    skumm_man

spelare: egenskaper
    egenskaper

egenskaper: arvet
    namn
    hp
    level
    skada

attack
    skada

zombie = vill inte dö, 40 hp, 3, 5 dmg

skumm_man = trump, 3hp, 1, 0.1 dmg

spelare = spelare, 70hp, level, 10 dmg


while true:

    random monster
        monster attakerar spelare 
                -dmg
    spelare attakerar
        -dmg

 
    if spelare hp== 0:
        print att spalre förlorar
        break
        
    if monster hp == 0:
        print att monster förlorar
        break


