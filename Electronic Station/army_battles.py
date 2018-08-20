class Warrior:
    health = 50
    damage = 5
    is_alive = True


class Knight(Warrior):
    damage = 7


def fight(first_unit, second_unit):
    while second_unit.is_alive and first_unit.is_alive:
        second_unit.health -= first_unit.damage
        second_unit.is_alive = second_unit.health > 0
        if second_unit.is_alive:
            first_unit.health -= second_unit.damage
            first_unit.is_alive = first_unit.health > 0
        else:
            return True
        if not first_unit.is_alive:
            return False


class Army:
    def __init__(self):
        self.army = []

    def add_units(self, kind, amount):
        for _ in range(amount):
            self.army.append(kind())


class Battle:
    def fight(self, army_1, army_2):
        while len(army_1.army) and len(army_2.army):
            if fight(army_1.army[0], army_2.army[0]):
                army_2.army.pop(0)
            else:
                army_1.army.pop(0)
        if len(army_1.army):
            return True
        else:
            return False


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)


army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

assert battle.fight(my_army, enemy_army) == True
assert battle.fight(army_3, army_4) == False
print("Coding complete? Let's try tests!")
