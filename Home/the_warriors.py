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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
