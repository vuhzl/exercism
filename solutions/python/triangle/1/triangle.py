def equilateral(sides):
    new_sides = set(sides)
    if all(new_sides) == 0:
        return False
    if len(new_sides) == 1:
        return True
    return False


def isosceles(sides):
    new_sides = set(sides)
    if len(new_sides) == 1:
        return True
    if len(new_sides) == 2:
        siides = sorted(new_sides)
        if siides[0] * 2 >= siides[-1]:
            return True
    return False


def scalene(sides):
    new_sides = set(sides)
    if len(new_sides) == 1:
        return False
    if len(new_sides) == 2:
        siides = sorted(new_sides)
        if siides[0] * 2 >= siides[-1]:
            return False
    if len(new_sides) == 3:
        siides = sorted(new_sides)
        if (siides[0] + siides [1] >= siides[2]):
            return True
    return False
